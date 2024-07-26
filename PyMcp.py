import os
import json
mcp = json.load(open(r"C:/Users/Administrator/Desktop/mcp.txt"))
print("Succ Load...")
for root, dirs, files in os.walk(r"D:\forge projects\1.20.1 RBW Now\src\main\java\craftedegg\rbw"):
    for file in files:
        if ".java" in file or ".json" in file:
            f = open(os.path.join(root, file), encoding="latin1").read()
            print("LOADING:", os.path.join(root, file))
            for k in mcp.keys():
                if k in f:
                    print("Srg", k, "MCP", mcp[k])
                    f = f.replace(k, mcp[k])

            open(os.path.join(root, file), 'w', encoding="latin1").write(f)
            print("Write Succ:", os.path.join(root, file))