# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:root
# datetime:19-3-12 上午11:26
# software: PyCharm
import xlwt
import re
import os
import multiprocessing


def trans(log_path, log_xls_path, log_name):
	"""

	:param log_path:
	:param log_xls_path:
	:param log_name:
	:return:
	"""
	with open(log_path + log_name, "r", encoding='ANSI') as f:
	# 注意读文件时编码与文件编码一致
		line_list = f.readlines()
	full_list = re.split(r'[;\s]', line_list[0])
	print(full_list)
	print(len(full_list))

	workbook = xlwt.Workbook(encoding='utf-8')
	sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
	sheet1.write(0, 0, '日期')
	sheet1.write(0, 1, '时间')

	# 需要完整表头

	row = 1
	for line in line_list:
		column = 0
		full_list = re.split(r'[;\s]', line)

		# 将来在这里替换、删除不要的full_list元素

		for data in full_list:
			sheet1.write(row, column, data)
			column += 1
		row += 1
	workbook.save(log_xls_path + log_name[:-4] + '.xls')


def logNameList(log_dir):
	for path, sub_dirs, filenames in os.walk(log_dir):
		print(path)
		print(sub_dirs)
		print(filenames)
		return filenames


if __name__ == '__main__':
	log_path = r'C:\Users\Administrator\Desktop\pyfirewalllog\log\\'
	log_xls_path = r'C:\Users\Administrator\Desktop\pyfirewalllog\logxls\\'
	log_name_list = logNameList(log_path)
	pool = multiprocessing.Pool(3)
	for log_name in log_name_list:
		pool.apply_async(trans, (log_path, log_xls_path, log_name,))
	pool.close()
	pool.join()
