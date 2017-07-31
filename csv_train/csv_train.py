#csv_train.py - Processing train.csv
import csv,os
train_file=open('train.csv')
train_reader=csv.reader(train_file)
for row in train_reader:                                          #循环读取train文件
    print('Row #' + str(train_reader.line_num)+' '+str(row))