def tpVector(lines):
  N = len(lines)
  tp = []
  for i in range(N):
    if (len(lines[i]) > 0):
      tp.append(0)
    else:
      tp.append(1)
  return tp