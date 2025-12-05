import sys
from itertools import cycle


def main():
    part2 = 0

    mapping = {}
    instructions = next(sys.stdin).rstrip()
    next(sys.stdin)

    mapping = { line[:3]: (line[7:10], line[12:15]) for line in sys.stdin}

    print("digraph {")
    print("  subgraph green {");
    for node in mapping.keys():
        if node[2] == "A":
            print(f'    {node} [fontcolor="white" fillcolor="green" style="filled"]')
    print("  }");
            
    print("  subgraph red {");
    for node in mapping.keys():
        if node[2] == "Z":
            print(f'    {node} [fontcolor="white" fillcolor="red" style="filled"]')
    print("  }");

    for node, (end1, end2) in mapping.items():
        # print(f'  {node} [color="green"] -> {{{end1}, {{{end2}}};')
        print(f'  {node} -> {{{end1}, {end2}}};')
    print("}")

    quit()

    nodes = [node for node in mapping.keys() if node[2] == "A"]
    for node in nodes:
        seen = {node}

        print(node)
        x = 0
        for i, instruction in enumerate(cycle(instructions), 1):
            node = mapping[node][instruction == "R"]
            if node[2] == "Z":
                print(i)

                x += 1
                if x == 5:
                    break
        print(i / 5)
        print()




    # for i, instruction in enumerate(cycle(instructions), 1):
    #     nodes = [mapping[node][instruction == "R"] for node in nodes]
    #     if all(node[2] == "Z" for node in nodes):
    #         break

    print(i)
    print(part2)


if __name__ == "__main__":
    main()
