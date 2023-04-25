import anytree as cay
from anytree import Node, RenderTree, NodeMixin

#Tạo Node với các giá trị cố định (Tên, Children, hàm append)
class Node:
    def __init__(self, ten):
        self.ten = ten #Giá trị tên Node
        self.children = [] #Giá trị con của Node

    def them_cay(self, node):
        self.children.append(node) #Thêm cây

def tao_cay():
    root_value = input("Nhập giá trị gốc: ")
    root = Node(root_value) #Cho giá trị gốc với các giá trị cố định vào trong biến "root"
    node_queue = [root] #Tạo một hàng đợi Node với giá trị đầu là "Root"
    while len(node_queue) > 0: #Điều kiện hàng đợi lớn hơn 0
        current_node = node_queue.pop(0) #Lấy phần tử đầu tiên trong hàng đợi làm "Node hiện tại"
        num_children = int(input(f"Nhập số lượng con của gốc {current_node.ten}: ")) #Số lượng con của Node hiện tại
        for i in range(num_children):
            goc_2 = current_node.ten #Thêm biến goc_2 nhằm miêu tả rõ hơn lệnh input
            child_value = input(f"Giá trị con thứ {i+1} của gốc {goc_2}: ") #Lấy giá trị i+1, bởi vì biến current_node đang nằm ở vị trí i = 0
            #Cho giá trị con với các giá trị cố định vào trong biến "child_node"
            child_node = Node(child_value)
            #Gọi hàm "them_cay" để thêm giá trị "con" vào "Node hiện tại"
            current_node.them_cay(child_node)
            #Thêm giá trị "con" vào hàng đợi
            node_queue.append(child_node)

    return root #Trả lại toàn bộ giá trị của cây 

goc = tao_cay()

for pre, _, node in RenderTree(goc):
    print("%s%s" % (pre, node.ten)) #Sử dụng thư viện "anytree" với "RenderTree" để tạo cây

#Duyệt theo thứ tự sau
def duyet_theo_thu_tu_sau(node):
    if node is not None:
        for children in node.children:
            duyet_theo_thu_tu_sau(children)
        print(node.ten)
print("Duyệt theo thứ tự sau: ")    
duyet_theo_thu_tu_sau(goc)

#Duyệt theo thứ tự trước:
def duyet_theo_thu_tu_truoc(node):
    if node is not None:
        print(node.ten)
        for children in node.children:
            duyet_theo_thu_tu_truoc(children)
print("Duyệt theo thứ tự trước: ")      
duyet_theo_thu_tu_truoc(goc)