import DS18B20 as ds
import time

sensor = ['28-0117C19740FF', '28-0117C1AFC0FF', '28-0217C11EE0FF',
          '28-0217C12228FF', '28-0117C17354FF', '28-0217C1129CFF',
          '28-0117C14282FF', '28-0117C19E86FF', '28-0117C140A6FF',
          '28-0217C1426EFF', '28-0217C1283EFF', '28-0117C1747EFF',
          '28-0117C1757EFF', '28-0217C10009FF', '28-0117C16769FF',
          '28-0117C17799FF', '28-0217C13A79FF', '28-0217C0FD79FF',
          '28-0117C16F35FF', '28-0117C17A75FF', '28-0217C1B8CDFF',
          '28-0117C17B2DFF', '28-0217C14203FF', '28-0117C16783FF',
          '28-0217C0FB8BFF', '28-0217C0FCEBFF', '28-0217C1B35BFF',
          '28-0117C190E7FF', '28-0117C19757FF', '28-0217C1146FFF']


ds.pinsStartConversion([21])
time.sleep(0.75)
for i in range(len(sensor)):
  print("{}- {} : {} 'C".format(i+1,sensor[i],ds.read(False,21,sensor[i])))


