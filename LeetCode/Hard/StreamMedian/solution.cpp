class MedianFinder
{
public:
    /** initialize your data structure here. */
    priority_queue<int> max_heap;
    priority_queue<int, vector<int>, greater<int>> min_heap;
    double median;
    int sz_max, sz_min;

    MedianFinder()
    {
        median = 0.0;
        sz_max = 0, sz_min = 0;
    }

    void addNum(int num)
    {
        if (num > median)
        {
            // Insert to min
            min_heap.push(num);
            sz_min++;
        }
        else
        {
            // Insert to max
            max_heap.push(num);
            sz_max++;
        }

        // Rebalance the 2 queues
        rebalance();
        median = findMedian();
    }

    double findMedian()
    {
        if (sz_min > sz_max)
        {
            return (double)min_heap.top();
        }
        else if (sz_min < sz_max)
        {
            return (double)max_heap.top();
        }
        else
        {
            return ((double)min_heap.top() + (double)max_heap.top()) / 2.0;
        }
    }

    void rebalance()
    {
        if (abs(sz_min - sz_max) > 1)
        {
            if (sz_min > sz_max)
            {
                // Get the top most item and insert to max
                max_heap.push(min_heap.top());
                min_heap.pop();
                sz_min--;
                sz_max++;
            }
            else
            {
                // Get the top most item and insert to min
                min_heap.push(max_heap.top());
                max_heap.pop();
                sz_min++;
                sz_max--;
            }
        }
    }
};
