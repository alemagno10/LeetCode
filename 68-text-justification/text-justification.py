from copy import deepcopy

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line, lenght = [], 0

        for i,w in enumerate(words):
            if len(w) + lenght <= maxWidth:
                lenght += len(w)+1
                line.append(w)
            else:
                lines.append(deepcopy(line))
                line = [w]
                lenght = len(w)+1
        
        if line:
            lines.append(deepcopy(line))
        
        output = []
        for i,line in enumerate(lines):
            lenght = sum(map(lambda x: len(x), line))
            spaces = maxWidth - lenght

            if len(line) == 1 or len(lines) == i+1:
                output.append(" ".join(line)+" "*(spaces-len(line)+1))
            else:
                text = ""
                for k,w in enumerate(line):
                    cspaces = math.ceil(spaces/(len(line)-k-1)) if len(line)-k-1 > 0 else 0
                    text += w + " "*cspaces
                    spaces -= cspaces
                output.append(text)
        
        return output



        





        
# paragraphs = [cline]
# maxW = 16, 
# line = ["This", "is", "an"], len = 8
