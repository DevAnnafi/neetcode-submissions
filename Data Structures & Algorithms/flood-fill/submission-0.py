class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r,c):
            # Base Check - Out of Bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 

            # Base Check 2 - Does not match the original color
            if image[r][c] != original_color:
                return

            # Flip the color
            image[r][c] = color

            # Recursive calls
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr,sc)
        return image

