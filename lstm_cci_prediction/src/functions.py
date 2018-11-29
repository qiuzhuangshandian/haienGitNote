
from mxnet import nd,autograd,gluon
from mxnet.gluon import loss as gloss
import time,math,csv
from src.config import paramPath,lossPath

def get_params(num_inputs,num_hiddens,num_outputs,ctx):
    def _one(shape):
        return nd.random.normal(scale=0.01, shape=shape, ctx=ctx)

    def _three():
        return (_one((num_inputs, num_hiddens)),
                _one((num_hiddens, num_hiddens)),
                nd.zeros(num_hiddens, ctx=ctx))

    W_xi, W_hi, b_i = _three()  # 输入门参数。
    W_xf, W_hf, b_f = _three()  # 遗忘门参数。
    W_xo, W_ho, b_o = _three()  # 输出门参数。
    W_xc, W_hc, b_c = _three()  # 候选细胞参数。
    # 输出层参数。
    W_hq = _one((num_hiddens, num_outputs))
    b_q = nd.zeros(num_outputs, ctx=ctx)
    # 创建梯度。
    params = [W_xi, W_hi, b_i, W_xf, W_hf, b_f, W_xo, W_ho, b_o, W_xc, W_hc,
              b_c, W_hq, b_q]
    for param in params:
        param.attach_grad()
    return params

def init_lstm_state(batch_size, num_hiddens, ctx):
    return (nd.zeros(shape=(batch_size, num_hiddens), ctx=ctx),
            nd.zeros(shape=(batch_size, num_hiddens), ctx=ctx))

def lstm(inputs, state, params):
    [W_xi, W_hi, b_i, W_xf, W_hf, b_f, W_xo, W_ho, b_o, W_xc, W_hc, b_c,
     W_hq, b_q] = params
    (H, C) = state
    outputs = []
    for X in inputs:
        # print(X.shape,W_xi.shape,H.shape,W_hi.shape,b_i.shape)
        I = nd.sigmoid(nd.dot(X, W_xi) + nd.dot(H, W_hi) + b_i)
        F = nd.sigmoid(nd.dot(X, W_xf) + nd.dot(H, W_hf) + b_f)
        O = nd.sigmoid(nd.dot(X, W_xo) + nd.dot(H, W_ho) + b_o)
        C_tilda = nd.tanh(nd.dot(X, W_xc) + nd.dot(H, W_hc) + b_c)
        C = F * C + I * C_tilda
        H = O * C.tanh()
        Y = nd.dot(H, W_hq) + b_q
        outputs.append(Y)
    return outputs, (H, C)

def sgd(params, lr, batch_size):
    """Mini-batch stochastic gradient descent."""
    for param in params:
        param[:] = param - lr * param.grad / batch_size

def init_momentum_states(params):
    # v_w = nd.zeros((features.shape[1], 1))
    # v_b = nd.zeros(1)
    states = []
    for param in params:
        states.append(nd.zeros_like(param))
    return states

def sgd_momentum(params, states, hyperparams):
    for p, v in zip(params, states):
        v[:] = hyperparams['momentum'] * v + hyperparams['lr'] * p.grad
        p[:] -= v

def grad_clipping(params, theta, ctx):
    """Clip the gradient."""
    if theta is not None:
        norm = nd.array([0.0], ctx)
        for param in params:
            norm += (param.grad ** 2).sum()
        norm = norm.sqrt().asscalar()
        if norm > theta:
            for param in params:
                param.grad[:] *= theta / norm
def SaveParams(params,saveDir):
    nd.save(saveDir,params)

def train_rnn(rnn, params, init_rnn_state, num_hiddens,ctx,
                          data_iter, num_epochs,lr,momentum,
              clipping_theta,batch_size, num_steps,pred_period):

    loss = gloss.L2Loss()  #l2 loss
    momentumStates = init_momentum_states(params)
    hyperparams = {"lr":lr,"momentum":momentum}
    lossRecord = []
    fw = open(lossPath, "w", newline="")
    csvWriter = csv.writer(fw, dialect="excel")
    csvWriter.writerow(["epoch","mean loss"])
    for epoch in range(num_epochs):
        state = init_rnn_state(batch_size, num_hiddens, ctx)
        loss_sum, start = 0.0, time.time()
        trainiter = data_iter(batch_size)
        if epoch > 500:
            lr = lr*0.9999
        for t, (X, Y) in enumerate(trainiter):
            X = nd.transpose(X,axes=[1,0,2])
            for s in state:
                s.detach()
            with autograd.record():
                (outputs, state) = rnn(X, state, params)
                outputs = nd.concat(*outputs, dim=0).reshape((-1,))
                y = Y.T.reshape((-1,))
                l = loss(outputs, y).mean()
            l.backward()
            grad_clipping(params, clipping_theta, ctx)
            # sgd(params, lr, 1)
            sgd_momentum(params=params,states=momentumStates,hyperparams=hyperparams)
            loss_sum += l.asscalar()

        if (epoch + 1) % pred_period == 0:
            SaveParams(params,saveDir=paramPath)
            print('epoch %d, average loss %f, time %.2f sec,lr: %f' % (
                epoch + 1, loss_sum / (t + 1), time.time() - start,lr))
        # lossRecord.append(loss_sum / (t + 1))
        csvWriter.writerow([epoch+1,loss_sum / (t + 1)])
    fw.close()



def PredictResult(X,rnn,params,batch_size,num_hiddens,ctx):
    X = nd.transpose(X, axes=[1, 0, 2])
    state = init_lstm_state(batch_size, num_hiddens, ctx)
    (outputs, state) = rnn(X, state, params)
    return outputs[-1]

def LoadParams(fname):
    return nd.load(fname)