class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // a window of 3 cannot have flowers
        for(int i = 0; i < flowerbed.size(); i++){
            // if current is occupied then skip
            if (flowerbed[i] == 1) continue;
            // if prev is occupied then skip
            if (i-1 >= 0 && flowerbed[i-1] == 1) continue;
            // if next is occupied we cannot plant
            if (i+1 < flowerbed.size() && flowerbed[i+1] == 1) continue;
            flowerbed[i] = 1;
            n--;
        }

        return n <= 0;
    }
};