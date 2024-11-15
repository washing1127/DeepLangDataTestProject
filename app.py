'''
Author: washing1127
Date: 2024-11-15 11:14:52
LastEditors: washing1127
LastEditTime: 2024-11-15 11:25:40
FilePath: /DeepLangDataTestProject/app.py
Description: 
'''
import gradio as gr
import traceback

import re


def hello_world_fn(username: str) -> tuple[str, str]:
    try:
        return f"HELLO WORLD\n{username.upper()}", "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"

def html_parser(html: str) -> list[str, str]:
    try:
        res = list()
        html = re.sub("\s*", "", html)
        idx = 0
        print("html",html)
        for i in range(len(html)):
            if html[i-3:i] == "<p>":
                idx = i
            elif html[i-4:i] == "</p>":
                res.append(html[idx: i-4])
        print("res", res)
        for idx, item in enumerate(res):
            res[idx] = re.sub("<.*>", "", item)
        print("res", res)
        return res
        # print(html)
        # res = re.findall("<p>(.*?)</p>", html)
        # print(res)
        # return res
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"

def main() -> None:
    with gr.Blocks(title="DeepLang Data test project") as demo:
        with gr.Tab("hello world 0"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 1"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )
            
        with gr.Tab("html parser"):
            raw_input = gr.Textbox(lines=15, placeholder="输入html", label="")
            pack_output = gr.Textbox(label="输出")
            # status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=html_parser,
                inputs=raw_input,
                outputs=[pack_output]#, status_output],
            )

    demo.queue(default_concurrency_limit=100).launch(
        inline=False,
        debug=False,
        server_name="127.0.0.1",
        server_port=8081,
        show_error=True,
    )


if __name__ == "__main__":
    main()
