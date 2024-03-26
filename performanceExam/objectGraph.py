import objgraph

class MyRefClass(object):
    pass

class C(object):
    pass

def main():
    ref1 = MyRefClass()

    c_objects = []
    for i in range(100):
        c = C()
        c.ref = ref1
        c_objects.append(c)

    # objgraph를 사용하여 참조 그래프 시각화
    objgraph.show_refs([c_objects[0]], filename='sample-graph.png')  # 첫 번째 C 객체에 대한 참조 그래프
    # objgraph.show_backrefs([c_objects[0]], filename='sample-backgraph.png')  # 필요한 경우 역참조 그래프

if __name__ == "__main__":
    main()