#include <iostream>
#include <unordered_map>

using namespace std;
class resetArray {
    /*
     * get - O(1)
     * set - O(1)
     * setAll - O(1)
     * an indexed data structure that has a fast reset all time!
     */
    struct pair {
        int version;
        int value;
    };

    public:
    int version;
    int resetValue;
    unordered_map<int, pair> values;

    resetArray(int startValue) {
        // must start at one because the ints start at 0 in the pair
        version = 1;
        resetValue = startValue;
    }

    void set(int index, int value) {
        pair newPair;
        newPair.version = version;
        newPair.value = value;
        values[index] = newPair;
    }

    void setAll(int value) {
        version++;
        resetValue = value;
    }

    int get(int index) {
        if (values[index].version != version) {
            return resetValue;
        }
        return values[index].value;
    }
};


int main() {
    resetArray arr(5);
    // 5
    std::cout << arr.get(3) << std::endl;
    // 5
    std::cout << arr.get(0) << std::endl;

    // 3
    arr.set(7, 3);
    std::cout << arr.get(7) << std::endl;

    // 9
    arr.setAll(9);
    std::cout << arr.get(7) << std::endl;
    std::cout << arr.get(1) << std::endl;

    // 8
    arr.set(3, 8);
    arr.set(7,8);
    std::cout << arr.get(3) << std::endl;
    std::cout << arr.get(7) << std::endl;

    return 0;
}
