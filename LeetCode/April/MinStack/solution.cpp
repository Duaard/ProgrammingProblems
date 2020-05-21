class MinStack
{
public:
    stack<pair<int, int>> s;

    MinStack()
    {
    }

    void push(int x)
    {
        if (s.size() > 0)
        {
            s.push({x, min(x, s.top().second)});
        }
        else
        {
            s.push({x, x});
        }
    }

    void pop()
    {
        if (s.size() != 0)
        {
            s.pop();
        }
    }

    int top()
    {
        return s.top().first;
    }

    int getMin()
    {
        return s.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */