from mxnet import nd,cpu
from src.functions import  get_params,init_lstm_state,lstm,train_rnn
from src.config import num_steps,num_epochs,lr,clipping_theta,batch_size,pred_period,momentum,featureNumber,num_hiddens,num_outputs
from src.SetReader import TrainSetIter

#the length of input vector,number of units in hidden layer, the length of output vector
# num_inputs, num_hiddens, num_outputs,num_steps = 16, 50, 1,5

ctx = cpu(0)
params = get_params(num_inputs=featureNumber,num_hiddens=num_hiddens,num_outputs=num_outputs,ctx=ctx)

train_rnn(lstm, params, init_lstm_state,
          num_hiddens,ctx,TrainSetIter,
          num_epochs,lr,momentum, clipping_theta,
          batch_size,num_steps, pred_period)


print("OK!")






