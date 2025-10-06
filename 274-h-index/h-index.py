class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        citations[i] is the number of citations a researcher received for 
        his ith paper
        h-index => max val of h such that he has published at least h papers
        that have each been cited at least h times

        citations = [3,0,6,1,5]
        h = 5 ? => at least 5 papers that have each been cited at least 5 times
                   ans: no
        
        paper_count = [1, 1, 0, 1, 0, 2]
                    
        """
        paper_count = [0] * (len(citations) + 1) # min is h=0 and max is h=6
        for i in range(len(citations)):
            if citations[i] >= len(citations):
                paper_count[len(citations)] += 1
            else:
                paper_count[citations[i]] += 1
        
        h_index = len(citations)
        count = 0
        res = 0

        while h_index > 0:

            count += paper_count[h_index]
            print(count)
            if count >= h_index:
                res = max(res, h_index)
            h_index -= 1
        
        return res