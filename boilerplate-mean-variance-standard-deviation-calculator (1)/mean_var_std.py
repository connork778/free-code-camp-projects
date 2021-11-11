import numpy as np

def calculate(elements):
  if len(elements) < 9:
    raise ValueError("List must contain nine numbers.")
    
  
  matrix = np.array(elements)
  matrix = matrix.reshape((3, 3))

  calculations = {}
  calc_mean = []
  calc_mean.append(np.mean(matrix, axis=(0)).tolist())
  calc_mean.append(np.mean(matrix, axis=(1)).tolist())
  calc_mean.append(np.mean(matrix).tolist())
  calculations['mean'] = calc_mean

  calc_var = []
  calc_var.append(np.var(matrix, axis=(0)).tolist())
  calc_var.append(np.var(matrix, axis=(1)).tolist())
  calc_var.append(np.var(matrix).tolist())
  calculations['variance'] = calc_var

  calc_std = []
  calc_std.append(np.std(matrix, axis=(0)).tolist())
  calc_std.append(np.std(matrix, axis=(1)).tolist())
  calc_std.append(np.std(matrix).tolist())
  calculations['standard deviation'] = calc_std

  calc_max = []
  calc_max.append(np.max(matrix, axis=(0)).tolist())
  calc_max.append(np.max(matrix, axis=(1)).tolist())
  calc_max.append(np.max(matrix).tolist())
  calculations['max'] = calc_max

  calc_min = []
  calc_min.append(np.min(matrix, axis=(0)).tolist())
  calc_min.append(np.min(matrix, axis=(1)).tolist())
  calc_min.append(np.min(matrix).tolist())
  calculations['min'] = calc_min

  calc_sum = []
  calc_sum.append(np.sum(matrix, axis=(0)).tolist())
  calc_sum.append(np.sum(matrix, axis=(1)).tolist())
  calc_sum.append(np.sum(matrix).tolist())
  calculations['sum'] = calc_sum

  return calculations