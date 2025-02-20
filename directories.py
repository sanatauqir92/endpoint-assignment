class Node:
  def __init__(self, name):
    self.name = name
    self.children = []

class Tree:
  def __init__(self, root_data):
    self.root = Node(root_data)

  def add_child(self, parent_data, child_data):
    parent_node = self._find_node(self.root, parent_data)
    
    if parent_node:
        parent_node.children.append(Node(child_data))
        parent_node.children.sort(key=lambda x:x.name)
    else:
        raise ValueError("Parent node not found")
    
  def remove_child(self, parent_name, child_name):
    if not parent_name:
      return None
    
    parent_node = self._find_node(self.root, parent_name)

    if not parent_node.children and parent_name == child_name:
      return None
  
    if parent_node.children:
      parent_node.children = [
        child for child in parent_node.children if child.name != child_name
      ]
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
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
DELETE fruits/apples
DELETE foods/fruits/apples
LIST"""

def parse_input(input):
  directoryTree = Tree('root')
  for line in input.splitlines():
    print(line)
    s_line = line.split()
    choice = s_line[0]
    match choice:
      case "CREATE":
        new_directory = s_line[1] if (len(s_line) > 1) else ""
        if "/" in new_directory:
          split = new_directory.split("/")
          directoryTree.add_child(split[len(split)-2], split[len(split)-1])
        else:
          directoryTree.add_child('root', new_directory)
      case "LIST":
        directoryTree.display()
      case "MOVE":
        out_directory = ""
        clean_directory = ""
        if "/" in s_line[1]:
          split = s_line[1].split("/")
          out_directory = split[len(split)-1]
          clean_directory = split[0]
          in_directory = s_line[2]
          directoryTree.add_child(in_directory, out_directory)
          directoryTree.remove_child(clean_directory, out_directory)
      case _:
        return

parse_input(input)
    