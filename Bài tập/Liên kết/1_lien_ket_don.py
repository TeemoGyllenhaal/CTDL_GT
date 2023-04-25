class Node: # tạo các nút (node) cho danh sách liên kết
    def __init__(self, data):
        self.data = data # lưu giá trị của nút
        self.next = None # lưu con trỏ đến nút tiếp theo trong danh sách

# Tạo danh sách liên kết đơn
class SinglyLinkedList:
    def __init__(self):
        self.head = None # lưu nút đầu tiên trong danh sách

    def append(self, data): # thêm một nút mới vào cuối danh sách liên kết
        new_node = Node(data) # tạo một đối tượng Node mới với giá trị được truyền vào data
        if self.head is None: ## kiểm tra nếu self.head bằng None, tức là danh sách liên kết ĐANG TRỐNG
            self.head = new_node # cập nhật self.head bằng nút mới
            return # kết thúc phương thức
        current = self.head ## nếu danh sách KHÔNG TRỐNG, duyệt từ đầu tới cuối danh sách = một biến current được khởi tạo bằng self.head
        while current.next:
            current = current.next # di chuyển current đến nút tiếp theo
                                   # sau khi vòng lặp kết thúc, current sẽ trỏ đến nút cuối cùng của danh sách
        current.next = new_node # thêm nút mới vào cuối danh sách

    def prepend(self, data): # thêm một nút mới vào đầu danh sách liên kết
        new_node = Node(data) # tạo một đối tượng Node mới với giá trị được truyền vào data
        new_node.next = self.head # nút mới sẽ trỏ đến nút đầu tiên của danh sách
        self.head = new_node # cập nhật self.head bằng nút mới, để đảm bảo rằng nút mới đã trở thành nút đầu tiên của danh sách

    def print_list(self): # in ra các giá trị của các nút trong danh sách liên kết
        current = self.head # khởi tạo biến current bằng nút đầu tiên của danh sách liên kết
        while current: # duyệt qua danh sách liên kết. Trong mỗi lần lặp ...
            print(current.data) # ... in ra giá trị của nút hiện tại
            current = current.next # di chuyển đến nút tiếp theo của danh sách liên kết
            # Vòng lặp sẽ tiếp tục cho đến khi current bằng None
            # tức đã duyệt hết danh sách liên kết và in ra tất cả các giá trị của các nút trong danh sách

# Tạo danh sách liên kết đơn
linked_list = SinglyLinkedList()

# Thêm các giá trị vào danh sách
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)

# In ra các giá trị trong danh sách
linked_list.print_list()  # Kết quả: 0 1 2 3
