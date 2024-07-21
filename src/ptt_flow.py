import glob
import os

import pandas as pd

# Define Function

columns = [
    '推',
    '噓',
    '分數',
    '作者',
    '標題',
    '時間'
]

def get_text_file_paths() -> list[str]:
    return glob.glob(
        '/workspaces/demo-devcontainer-main/res_gossiping/*.txt'
    )

def e_text_file(path: str)  -> str:                           # :參數型別    -> 回傳值的型別
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def  t_text_to_df_row_list(article_string: str) -> list[str]:
    reply_info_string = article_string.split('---split---')[1]
    return reply_info_string.split('\n')[1:-1]

def t_conbine_list_to_df(reply_info_lists: list[list]) -> pd.DataFrame:
    return pd.DataFrame(
        data=reply_info_lists,
        columns=columns
    )

# def l_df_to_csv(df: pd.DataFrame) -> None:
#     df.to_csv('ptt.csv', index=False)



if __name__ == '__main__':                         #  當其他程式 import這個模組時 不會實際執行
    # Get paths of all text files                  #  可以視作是範例 也是這支程式的主邏輯
    path_list = get_text_file_paths()

    # Loop for file path
    data = []
    for path in path_list:
        # Extract text file
        article_string = e_text_file(path)
        # Text to List_element in DataFrame
        reply_info_list = t_text_to_df_row_list(article_string)
        data.append(reply_info_list)
        # Concat lists of DataFrame
        df = t_conbine_list_to_df(data)
    # Load DataFrame to csv
    #  l_df_to_csv(df)
