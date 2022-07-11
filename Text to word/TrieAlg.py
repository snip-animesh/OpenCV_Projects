class Trie:
    head={}

    def insert(self,word):
        current_node=self.head

        for ch in word:
            if ch not in current_node:
                current_node[ch]={}
            current_node=current_node[ch]
        current_node['*']=True

    def search(self,word):
        current_node=self.head

        for ch in word:
            if ch not in current_node:
                return False
            current_node=current_node[ch]
        if "*" in current_node:
            return True
        else:
            return False