'''
Author: Tim Liang

This tool is use for auto generate issue list and auto format.

para1: original issue sheet, *.csv export from Jira
para2[Optional]: issue number filter, number should be split by ','


df: means dataframe
Notes: this is using one fixed xlsx format with colume: ['Issue key','Summary','Assignee','Reporter','Priority','Status']
Be aware: the columes are hard code
'''

import os,sys,traceback,xlsxwriter
import pandas as pd
from datetime import datetime

class GenerateIsssueList():
    def __init__(self, original_file, filter_file):
        self.original_file = original_file
        self.filter_file = filter_file
        
    def read_original_file(self,file_name):
        '''
        original file is *.csv file
        this csv_data is Dataframe of pandas
        '''
        if "csv" in file_name:
            csv_data = pd.read_csv(file_name)
            
        else:
            print ("only *csv file is supported")
        
        return csv_data
        
    def read_filter_file(self,file_name):
        '''
        filter file is txt file or none
        '''
        list_issue_expected = []
        try:
            if file_name != None:
                f = open(file_name,'r')
                data = f.read()
                f.close()
                list_issue_expected = data.replace(" ","").split(',')
                #remove duplicated element
                list_issue_expected = list(set(list_issue_expected))
                
                print ("Expected issue list:%s"%list_issue_expected)
        except:
            list_issue_expected = []
            print(traceback.format_exc())

        return list_issue_expected
        
        
    def select_column(self,df_data):
        try:
            column_list = ['Issue key','Summary','Assignee','Reporter','Priority','Status']
            df_data = df_data[column_list]
        except:
            print(traceback.format_exc())
        
        return df_data
        
    def select_row(self,df_data, list_issue_expected=[]):
        '''
        1. get row number list
        2. geit row from df_data
        '''
        rst_df_data = df_data
        
        # create one new dataframe
        cols = df_data.columns.values
        df_data_seleted = pd.DataFrame(columns=cols)
        
        issue_key_column = df_data.columns.get_loc('Issue key')
        
        if list_issue_expected != []:
            for i in range(len(df_data)):
                issue_key = df_data.iloc[i,:][issue_key_column].split('-')[1]
                if issue_key in list_issue_expected:
                    df_data_seleted = df_data_seleted.append(df_data.iloc[i,:])
                    list_issue_expected.remove(issue_key)
            rst_df_data = df_data_seleted
        else:
            print("no issue number in filter, all issues selected")
        
        #print issue not in the original list
        if list_issue_expected != []:
            print ("This issues are not in the original file: %s"%list_issue_expected)

        return rst_df_data
        
    def create_output_excel(self,df_data):
        '''
        Create output excel and set first row to bolder
        Add Colume name, and set to bold
        set column to fit size
        Blocker,Critical,Major need to set to red
        '''
        #create a new work 
        workbook_name = "issue_list_%s.xlsx"%datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        workbook = xlsxwriter.Workbook(workbook_name)
        worksheet = workbook.add_worksheet('Issues')

        #format the colume width
        worksheet.set_column('A:A', 15)
        worksheet.set_column('B:B', 120)
        worksheet.set_column('C:C', 26)
        worksheet.set_column('D:D', 26)
        worksheet.set_column('E:E', 12)
        worksheet.set_column('F:F', 12)
        
        #set format
        red_format = workbook.add_format({
            'font_color': 'red',
            'border': 1,
            })

        bold_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            })
            
        hyperlink_format = workbook.add_format({
            'font_color': 'blue',
            'underline':  1,
            'border': 1,})
            
        border_format = workbook.add_format({
            'border': 1,})

        #set front_size to 11
        

        
        # add colume name
        worksheet.write_string('A1', "Issue key", bold_format)
        worksheet.write_string('B1', "Summary", bold_format)
        worksheet.write_string('C1', "Assignee", bold_format)
        worksheet.write_string('D1', "Reporter", bold_format)
        worksheet.write_string('E1', "Priority", bold_format)
        worksheet.write_string('F1', "Status", bold_format)
        
        #write data to xlsx file
        #transform dataframe to list
        list_data = df_data.values.tolist()
        row_num = 2
        jira_issue_url = "https://jabra1.atlassian.net/browse/"
        
        for ele in list_data:
            # first colume: issue number with hyperlink
            worksheet.write_url('A%s'%row_num, jira_issue_url + str(ele[0]), hyperlink_format, string=ele[0])
            
            worksheet.write_string('B%s'%row_num, ele[1],border_format)
            worksheet.write_string('C%s'%row_num, ele[2],border_format)
            worksheet.write_string('D%s'%row_num, ele[3],border_format)
            #below is 'Priority' column
            if ele[4] in ['Blocker','Critical','Major']:
                worksheet.write_string('E%s'%row_num, ele[4],red_format)
            else:
                worksheet.write_string('E%s'%row_num, ele[4],border_format)
            worksheet.write_string('F%s'%row_num, ele[5],border_format)

            row_num = row_num +1

        workbook.close()
        
        return workbook_name

    def __test_output_df_to_csv(self,sf_data):
        '''
        this is for debug
        '''
        print (sf_data)
        sf_data.to_csv("test_output.csv")
    
    def generate_issue_list(self):
        csv_data = self.read_original_file(self.original_file)
        list_issue_expected = self.read_filter_file(self.filter_file)
        df_data = self.select_column(csv_data)
        df_data = self.select_row(df_data,list_issue_expected)
        workbook_name = self.create_output_excel(df_data)
        self.open_output_file(workbook_name)
        
    def open_output_file(self,file_name):
        '''
        auto open output file in excel
        '''
        try: 
            cmd = "start /MAX excel " + file_name
            os.system(cmd)
        except:
            print ("Fail to start excel application")


if __name__ == '__main__':
    original_file = sys.argv[1]
    if len(sys.argv) >= 3:
        filter_file = sys.argv[2]
    else:
        filter_file = None
    
    gene_ins = GenerateIsssueList(original_file, filter_file)
    gene_ins.generate_issue_list()