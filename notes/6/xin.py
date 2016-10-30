#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import os
while True:
	print '''		 \033[31;1m**************************************\033[0m
		 \033[31;1m*	1.Search		      *\033[0m
		 \033[31;1m*	2.Add、Del、Change	      *\033[0m
		 \033[31;1m**************************************\033[0m'''
	action = int(raw_input('Please enter the number of your needs? '))
	if action == 1:
		count_number = 0
		Action_One_Key = raw_input('Please enter a keyword query: ')
		F = file('staff.txt','r')
		for line in F.readlines():
			if Action_One_Key in line:
				count_number += 1
				line_strip = line.strip()
				print '\033[32;1m %s\033[0m' %line_strip
		print '\033[41;1mcount_number: %s\033[0m' %count_number
		Goon_key = raw_input('Do you want to continue? (y|n) ')
		if Goon_key == 'n':
			break
	elif action == 2:
		print '''                 \033[32;1m**************************************\033[0m
                 \033[32;1m*    1.Add                           *\033[0m
                 \033[32;1m*    2.Del                           *\033[0m
		 \033[32;1m*    3.Change                        *\033[0m
                 \033[32;1m**************************************\033[0m'''
		action_2 = int(raw_input('Please enter the number of your needs? '))
		if action_2 == 1:
			input_str = raw_input('Please enter the information you want to add employees: ')
			F_write = file('staff.txt','a')
			F_write.write('%s\n'%input_str)
			F_write.close()
			Goon_key = raw_input('Do you want to continue? (y|n) ')
                	if Goon_key == 'n':
                        	break
		elif action_2 == 2:
			del_str = raw_input('Please enter your user information to be deleted: ')
			F_del = file('staff.txt','r')
			F_del_new = file('staff_del_bak.txt','w')
			for line in F_del.readlines():
				if del_str in line:
					continue
				F_del_new.write(line)
			F_del.close()
			F_del_new.close()
			os.rename('staff_del_bak.txt','staff.txt')
			Goon_key = raw_input('Do you want to continue? (y|n) ')
                        if Goon_key == 'n':
                                break
		elif action_2 == 3:
			input_change_str = raw_input('Please enter your user information to be modified: ')
			input_change_str2 = raw_input('Please enter the modified content: ')
			F_change_source = file('staff.txt','r')
			F_change_new = file('staff_change_bak.txt','w')
			for line in  F_change_source.readlines():
				if input_change_str in line:
					line = line.replace(input_change_str,input_change_str2)
					print line
				F_change_new.write('%s\n'%line)
			F_change_source.close()
			F_change_new.close()
			os.rename('staff_change_bak.txt','staff.txt')
			Goon_key = raw_input('Do you want to continue? (y|n) ')
                        if Goon_key == 'n':
                                break
		else:
			print '\033[33;1m非法序列！请输入正确的操作符号！\033[0m'
	else:
		print '\033[33;1m非法序列！请输入正确的操作符号！\033[0m'

