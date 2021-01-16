import streamlit as st
import logging

from task import title, task

logger = logging.getLogger(__name__)


def detail_app():
    '''展示基金明细'''
    st.header(title)
    st.subheader("基金排行")
    col1, col2 = st.beta_columns(2)
    with col1:
        best_funds = st.checkbox("金选", True)
    fund_history = task.load(task.FUND_HISTORY_DATA_FILE)
    select_fund_code = task.load(task.SELECT_FUND_LIST_CODE_FILE)

    if best_funds:
        st.table(fund_history.loc[fund_history["基金代码"].isin(select_fund_code)].reset_index(drop=True))
    else:
        fund_history = fund_history.loc[fund_history["down_count"] > 3]
        fund_history.sort_values("RSI30", inplace=True)
        st.table(fund_history.reset_index(drop=True))


if __name__ == '__main__':
    detail_app()
