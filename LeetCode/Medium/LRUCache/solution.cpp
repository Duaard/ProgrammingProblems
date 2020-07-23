class LRUCache {
private:
    unordered_map<int, int> map;
    unordered_map<int, int> key_index;
    unordered_map<int, int> index_key;
    unordered_map<int, int> index_last;
    unordered_map<int, int> last_index;
    int latest;
    int load;
    int size;
    
    void updatePointers(int index, int last) {
        index_last[index] = last;
        last_index[last] = index;
    }
    
    void changeRecent(int index) {
        // Check if it's the first entry
        if(load == 0) {
            updatePointers(index, -1);
        } else if (index != latest) {
            // Update the index pointing to this index
            // to point at this_last, if there is one
            if(last_index.count(index)) {
                // Get the val this index is pointing to
                int this_last = index_last[index];
                int pointer_index = last_index[index];
                updatePointers(pointer_index, this_last);
            }

            // Point index to the latest
            updatePointers(index, latest);
        }
        
        // Change latest to index
        latest = index;
    }
    
    void evict(int key) {
        // Look for index pointing to -1
        int evict_index = last_index[-1];
        
        // Get the key of evicted val
        int evict_key = index_key[evict_index];
        
        // Give this key the index of the evicted val
        key_index[key] = evict_index;
        index_key[evict_index] = key;
        
        // Erase this from map
        map.erase(evict_key);
        key_index.erase(evict_key);
        
        // Update recent
        changeRecent(evict_index);
    }
public:
    LRUCache(int capacity) {
        load = 0;
        size = capacity;
    }
    
    int get(int key) {
        if (map.count(key)) {
            // Update recent using this index
            int index = key_index[key];
            changeRecent(index);
            
            // Return value
            return map[key];
        }
        
        return -1;
    }
    
    void put(int key, int value) {
        if(load < size && map.count(key) == 0) {
            // Input index for this key
            key_index[key] = load;
            index_key[load] = key;

            // Input value in our map
            map[key] = value;
            
            changeRecent(key_index[key]);
            
            // Increase load
            load++;
            
        } else if (map.count(key) != 0) {
            // Just update
            // Input value in our map
            map[key] = value;
            
            changeRecent(key_index[key]);
            
        } else {
            map[key] = value;
            
            // Evict value
            evict(key);            
        }
    }
};


/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
