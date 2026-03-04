import hashlib #Standard python library for cyptographic hashing
#Hash function like SHA-256 are one-way function: easy to compute,hard to reverse.
#Used here to create unique fingerprints of document for integrity vertification.
#Hash : a fixed-length unique fingerprint representing some data
class SecureDocument:
    def __init__(self,name,content = Name,student = None):
        self.name = name
        self.content = content or "" #Write or "" ensures the node always has a string,preventing error in hash computation if content is missing.
        self.student = student or [] #Similar logic as the self.content = content or ""
        self.hash = self.generate_hash() #Computes a fingerprint of this node and its subtree for furture integrity checks
    def generate_hash(self): #calculates a SHA-256 fingerprint using this node's conetnt plus all students
        combined = self.content
        for stud in self.student:
            combined += stud.hash
        return hash.lib.sha256(combined.encode()).hexdigest()) #converts content to bytes and creates a unique fingerprint for integrity vertification
        #return hash.lib.sha256(combined.encode()).hexdigest()) turn the string from human language into machine code
#Knowledge about this class Securedocument known by self-study.
class SecurityVertifier:
    def vertify(self,document):
        return self.vertify_recursive(document) #starts recursive check from root node
    def vertify_recursive(self,node):
        recalculated = node.content
        for stud in node.student: #veritify all child node
            if not self.vertify_recursive(stud): #if any student fail vertify,stop immediately
                return False
            recalculated += stud.hash #after child vertification,include its hash in parent's recompute
        recalculated  = hashlib.sha256(recalculated.encode()).hexdigest() #recalculate hash for this node
        if recalculated_hash != node.hash:
            print(f"Change of data detected in {node.name}")
            return False #any child tamper triggers in root invalidation
        return True 

