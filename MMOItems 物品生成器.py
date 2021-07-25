# 导入各类库
import easygui as gui
import os

forever = 1
while forever == 1:
    choice1 = gui.buttonbox("欢迎使用 FWEditor For MMO\n请选择您需要使用的功能", "FWEditor【v1.0.1 - Pre1】", choices=["生成完整yml文件", "生成空白yml文件", "更新日志"])
    print(choice1)
    if choice1 == '生成完整yml文件':
        f = open("result_completely.yml", "a")
        f.close()
        choice2 = gui.choicebox("请选择您想要生成的物品类别", "FWEditor【v1.0.1 - Pre1】", choices=["砍器类", "锐器类", "钝器类", "副手/双手武器类", "远程武器类", "其他", ], preselect=0)
        print(choice2)
        if choice2 == "砍器类":
            choice3 = gui.choicebox("请选择您想要生成的物品类别", "FWEditor【v1.0.1 - Pre1】", choices=["剑", "大剑", "太刀", "斧头", "巨斧", "戟", ], preselect=0)
        if choice2 == "其他":
            choice3 = gui.choicebox("请选择您想要生成的物品类别", "FWEditor【v1.0.1 - Pre1】", choices=["防具", "工具", "消耗品", "杂项", "宝石", "材料", ], preselect=0)
            if choice3 == "宝石":
                item = gui.multenterbox("请输入相应的信息，不设置则不填", "FWEditor【v1.0.1 - Pre1】", fields=["物品代号", "物品样式", "物品名称", "宝石颜色"])
                itemfilename = item[0]#物品标识名
                itemdisplay = item[1]#物品样式
                itemname = item[2]#物品显示名
                gemcolor = item[3]#宝石颜色
                f = open("result_completely.yml", "a")
                f.write(itemfilename + ":\n")
                f.write("   diaplay: " + itemdisplay + "\n")
                f.write("   name: '" + itemname + "'\n")
                f.write("   gem-color: '" + gemcolor + "'\n")
                f.close()
    elif choice1 == '生成空白yml文件':
        choice2 = gui.choicebox("请选择您想要生成的物品", "FWEditor【v1.0.1 - Pre1】", choices=["宝石", "其他"], preselect=0)
    elif choice1 == '更新日志':
        choice2 = gui.msgbox("功能开发中......[v1.0.1 - Pre1]", "Error!")
    else:
        close = gui.buttonbox("您是否真的要关闭该生成器？", "Close", choices=["确认", "取消"])
        if close != "取消":
            break