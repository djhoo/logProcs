# logProcs
process log and abstract useful information to xls by python
编译EXE命令：
pyinstaller -F -w log2csvVer1.py

版本说明：
Ver1：
1，以“state  curPos  curSpd  targSpd pid”为开头以下的所有数据 都生成一个csv
2，csv名字就是log名字后面加上.csv就行了

Ver2：
1，生成多个csv
2，以“jisstart”为开始的后面的 生成一个csv，名字是jisstart后面的数字
3，生成csv的内容就是 两个“jisstart”的内容

Ver3：
1，生成多个csv
2，以“jisstart”为开始的后面的 生成一个csv，名字是按照PID的I的数值
3，生成csv的内容就是 两个“jisstart”的内容
4，这个名字是从1/1到1/10000

Ver4：
1，生成多个csv
2，以“jisstart”为开始的后面的 生成一个csv，名字是按照PID的I的数值
3，生成csv的内容就是 两个“jisstart”的内容
4,  名字是1000,3000,5000,7000,10000,30000,50000,70000,100000

Ver5：
1，生成多个csv
2，以“jisstart”为开始的后面的 生成一个csv，名字是按照PID的I的数值
3，生成csv的内容就是 两个“jisstart”的内容
4,  名字是1/1000,1/3000,1/5000,1/7000,1/10000,1/30000,1/50000,1/70000,1/100000

Ver7:
1，生成多个xlsx
2，以“jisstart”为开始的后面的 生成一个xlsx，名字是按照PID的I的数值
3，生成xlsx的内容就是 以“jisstart”开头的文件
4,  文件名字是1/1000,1/3000,1/5000,1/7000,1/10000,1/30000,1/50000,1/70000,1/100000
5，xlsx里面有多个sheet，第一个sheet就是总的内容，后面的sheet就是分开的内容


Ver8:
1，生成多个xlsx
2，以“jisstart”为开始的后面的 生成一个xlsx，名字是按照PID的I的数值
3，生成xlsx的内容就是 以“jisstart”开头的文件
4,  这个名字是从1/1到1/10000
5，xlsx里面有多个sheet，第一个sheet就是总的内容，后面的sheet就是分开的内容
