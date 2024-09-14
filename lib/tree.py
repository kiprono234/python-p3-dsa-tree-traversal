class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, element_id):
    def search(node):
        if node['id'] == element_id:
            return node
        for child in node['children']:
            result = search(child)
            if result:
                return result
        return None

    return search(self.root)  
    pass
