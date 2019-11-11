#python3 encode.py ./test/test.txt ./encode.csv
#是否把几个固定计算机文件的路径作为参数输入？然后考到定向的位置？
import sys,os,shutil

input_file = sys.argv[1]
out_file = sys.argv[2]

shutil.rmtree("./temp")
os.mkdir("./temp")
#shutil.copy(input_file,"./decode/decode_file")


count=0;
for file in os.listdir(input_file):
	count=count+1
f_num=count-2 ##此处确立隐藏文件
#f_num=count-1
print(f_num)

#f_num=256

f_num =str(f_num)

cmd = "python ./lib/6_RSdecode.py "+input_file+"/encode_file_cod ./decode/decode_file_cod "+f_num
os.system(cmd)

for file in os.listdir("./decode/"):
	path="./decode/"+file
	sz = os.path.getsize(path)
	if sz == 0:
		os.remove(path)
		#print(path)

file_i=0
for file in os.listdir("./decode/"):
	file_i=str(file_i)
	file_name = "./temp/decode_file_cod"+file_i
	file = "./decode/" + file
	os.rename(file, file_name)
	file_i=int(file_i)
	file_i=file_i+1

cmd = "python ./lib/7_filter_decode.py ./temp/decode_file_cod "+f_num
os.system(cmd)
#以下不使用
#cmd = "python ./lib/8_check_encode.py ./decode/encode_file_cod "+f_num
#os.system(cmd)


shutil.copy("./encode/encode_file_meta.txt", "./temp/decode_file_meta.txt")

s = './temp/decode_file_meta.txt'
f1 = open(s, 'r')
old_lst = f1.readline()
#print(old_lst)
ls = old_lst.split(" ", 1)
lss="./temp/decode_file "+ls[1]
print(ls)
f1.close()
f2 = open(s, 'w')
f2.write(lss)
f2.close()


cmd = "F:\CODE\decode\lib/repair.exe ./temp/decode_file"
os.system(cmd)
#cmd = "F:\CODE\decode\lib/decode.exe ./temp/decode_file"
#os.system(cmd)
#shutil.copy("./decode/decode_file", out_file)

