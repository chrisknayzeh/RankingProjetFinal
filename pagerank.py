import numpy as np

def pagerank(edge_list, alpha, error, teleport):
  v = np.ones(len(edge_list))/len(edge_list)

  idx =0
  tp_times_v = []

  for item in teleport:
      tp_times_v.append(item*v[idx])
      idx+=1
      if idx > len(edge_list):
        break
  tp_times_v= np.array(tp_times_v)
  
  temp_v = np.zeros(len(edge_list))

  idx=0
  for item in edge_list:
      for i in item:
        temp_v[idx] += v[i-1]
      v[idx] = temp_v[idx]
      idx+=1
      if idx > len(edge_list):
        break

  temp_v = alpha*v + ((1-alpha)/len(edge_list))*tp_times_v

  iterations = 0
  while (np.linalg.norm(v-temp_v) > error):
    v = temp_v
    temp_v = alpha*v + ((1-alpha)/len(edge_list))*tp_times_v
    iterations +=1

  return v,iterations