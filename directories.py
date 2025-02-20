#input:
# CREATE fruits
# CREATE vegetables
# CREATE grains
# CREATE fruits/apples
# CREATE fruits/apples/fuji
# LIST
# CREATE grains/squash
# MOVE grains/squash vegetables
# CREATE foods
# MOVE grains foods
# MOVE fruits foods
# MOVE vegetables foods
# LIST
# DELETE fruits/apples
# DELETE foods/fruits/apples
# LIST

#output:
# CREATE fruits
# CREATE vegetables
# CREATE grains
# CREATE fruits/apples
# CREATE fruits/apples/fuji
# LIST
# fruits
#   apples
#     fuji
# grains
# vegetables
# CREATE grains/squash

#-------------------
# MOVE grains/squash vegetables
# CREATE foods
# MOVE grains foods
# MOVE fruits foods
# MOVE vegetables foods
# LIST
# foods
#   fruits
#     apples
#       fuji
#   grains
#   vegetables
#     squash
# DELETE fruits/apples
# Cannot delete fruits/apples - fruits does not exist
# DELETE foods/fruits/apples
# LIST
# foods
#   fruits
#   grains
#   vegetables
#     squash

class Node:
  def __init__(self, name):
    self.name = name
    self.children = []

#add node, find node, delete node, move node, print all
class Tree:
  def __init__(self, root_data):
    self.root = Node(root_data)

  def add_child(self, parent_data, child_data):
    parent_node = self._find_node(self.root, parent_data)
    #ideally instead of sorting the list each time, I would add each child node in sorted order
    if parent_node:
        parent_node.children.append(Node(child_data))
        parent_node.children.sort(key=lambda x:x.name)
    else:
        raise ValueError("Parent node not found")
  
  def _find_node(self, node, name):
    if node.name == name:
        return node
    for child in node.children:
        found_node = self._find_node(child, name)
        if found_node:
            return found_node
    return None

  def display(self, node=None, level = 0):
    if node is None:
      node = self.root
    if (level > 0):
      print(" " * (level-1) + str(node.name))
    for child in node.children:
      self.display(child, level + 1)


input = """CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
CREATE grains/squash"""

def parse_input(input):
  directoryTree = Tree('root')
  for line in input.splitlines():
    print(line)
    choice = line.split()[0]
    new_directory = line.split()[1] if (len(line.split()) > 1) else ""
    match choice:
      case "CREATE":
        if "/" in new_directory:
          split = new_directory.split("/")
          directoryTree.add_child(split[len(split)-2], split[len(split)-1])
        else:
          directoryTree.add_child('root', new_directory)
      case "LIST":
        directoryTree.display()
      case "MOVE":
        print(choice)
      case "DELETE":
        print(choice)
      case _:
        print('nope')


parse_input(input)
    