# coding = 'utf-8'
import numpy as np
import pandas as pd


def target_mean_v1(data, y_name, x_name):
   result = np.zeros(data.shape[0])
   for i in range(data.shape[0]):
       groupby_result = data[data.index != i].groupby([x_name], as_index=False).agg(['mean', 'count'])
       result[i] = groupby_result.loc[groupby_result.index == data.loc[i, x_name], (y_name, 'mean')]
   return result

def main():
   y = np.random.randint(2, size=(5000, 1))
   x = np.random.randint(10, size=(5000, 1))
   data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
   result_1 = target_mean_v1(data, 'y', 'x')


if __name__ == '__main__':
   main()



def target_mean_v4(data:pd.DataFrame, y_name:str, x_name:str) -> np.ndarray:
   data_shape = data.shape[0]
   result = np.zeros(data_shape)
   value_dict = dict()
   count_dict = dict()

x_val_series = data.loc[:, x_name]
   y_val_series = data.loc[:, y_name]
   for i in range(data_shape):
       data_loc_x = x_val_series[i]
       data_loc_y = y_val_series[i]
       if data_loc_x not in value_dict:
           value_dict[data_loc_x] = data_loc_y
           count_dict[data_loc_x] = 1
       else:
           value_dict[data_loc_x] += data_loc_y
           count_dict[data_loc_x] += 1
   for i in range(data_shape):
       data_loc_x = x_val_series[i]
       data_loc_y = y_val_series[i]
       result[i] = (value_dict[data_loc_x] - data_loc_y) / (count_dict[data_loc_x] - 1)

return result