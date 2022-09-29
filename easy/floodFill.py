class Solution: 
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]: return image
        target = image[sr][sc]
        def helper(r, c):
            if not (0 <= r < len(image) and 0 <= c < len(image[0])) or image[r][c] != target:
                return
            image[r][c] = color
            helper(r-1,c)
            helper(r+1,c)
            helper(r,c-1)
            helper(r,c+1)
        
        helper(sr,sc)
        return image
    
    """
    def floodFillI(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]: return image
        target = image[sr][sc]
        queue = [(sr,sc)]
        image[sr][sc] = color
        while queue:
            (r,c) = queue.pop()
            if 0 < r < len(image)-1:
                if image[r-1][c] == target:
                    image[r-1][c] = color
                    queue.append((r-1,c))
                if image[r+1][c] == target:
                    image[r+1][c] = color
                    queue.append((r+1,c))
            elif r > 0 and image[r-1][c] == target:
                image[r-1][c] = color
                queue.append((r-1,c))
            elif r < len(image)-1 and image[r+1][c] == target:
                image[r+1][c] = color
                queue.append((r+1,c))
            
            if 0 < c < len(image[0])-1:
                if image[r][c-1] == target:
                    image[r][c-1] = color
                    queue.append((r,c-1))
                if image[r][c+1] == target:
                    image[r][c+1] = color
                    queue.append((r,c+1))
            elif c > 0 and image[r][c-1] == target:
                image[r][c-1] = color
                queue.append((r,c-1))
            elif c < len(image)-1 and image[r][c+1] == target:
                image[r][c+1] = color
                queue.append((r,c+1))
        return image
    """
