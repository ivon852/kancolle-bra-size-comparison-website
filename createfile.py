import glob
ilist = glob.glob('./thumbnail/*.png')

for i in range(len(ilist)):
  f = open(ilist[i] +".meta", "w")
  f.write('{\n"Tags": ["Cup: A", "DD", "Kanmusu"],\n"Title": "",\n"ImageDescription": ""\n}')
  f.close()
