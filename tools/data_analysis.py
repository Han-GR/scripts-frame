import os

import pandas


class DataAnalysis:
    """数据分析类"""

    @staticmethod
    def write_excel(data_path, excel_name, excel_data):
        """
        data_path: 生成文件的保存路径
        excel_name: 表格名称
        excel_data: 表格数据,字典,例:{"名字": ["张三","李四"], "年龄": [11,12]}
        """
        os.makedirs(data_path, exist_ok=True)
        wait_write = pandas.DataFrame(excel_data)
        wait_write.to_excel(
            f"{data_path}{excel_name}.xlsx",
            sheet_name="Sheet1",
            index=False,
        )  # index = False表示不写入索引

    @staticmethod
    def read_excel(excel_path, fields=None, to_list=False):
        """
        excel_path: 要读取的文件路径
        fields: 要读取的字段列表,例:["姓名","年龄","性别"]
        to_list: 是否要将DataFrame,转换成列表返回
        return: DataFrame或者包含字典的列表
        """
        if fields is None:
            excel_data = pandas.read_excel(io=excel_path)
        else:
            excel_data = pandas.read_excel(io=excel_path, usecols=fields)
        data_list = excel_data.to_dict(orient="records")
        return excel_data if to_list is False else data_list

    @staticmethod
    def update_data(
        data_frame, condition_field, condition_value, update_field, update_value
    ):
        """
        data_frame: 使用pandas读取的数据格式
        condition_field: 筛选使用的条件字段
        condition_value: 筛选使用的条件值
        update_field: 要更新的字段
        update_value: 要更新的值
        return: 数据更新后的data_frame
        """
        data_frame.loc[
            data_frame[condition_field] == condition_value, update_field
        ] = update_value

        return data_frame
