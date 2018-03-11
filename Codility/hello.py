class Tree

{

    public int x;

    public Tree l;

    public Tree r;

};


class Task3

{

    public int solution(Tree T)

    {

        return FindZigZag(T, 0) - 1;

    }


    int FindZigZag(Tree t, int max)

    {

        if (t == null) return 0;


        int lh = Count(t, true, 0);

        int rh = Count(t, false, 0);


        max = Math.Max(lh, rh);

        max = Math.Max(max, FindZigZag(t.l, max));

        max = Math.Max(max, FindZigZag(t.r, max));


        return max;

    }


    int Count(Tree node, bool moveLeft, int count)

    {

        if (node == null) return count;


        count = moveLeft

            ? Count(node.l, !moveLeft, node.l == null ? count : count + 1)

            : Count(node.r, !moveLeft, node.r == null ? count : count + 1);


        return count;

    } 

}