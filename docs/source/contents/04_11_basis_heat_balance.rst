.. include:: definition.txt

.. raw:: latex

    \clearpage

========================================================================================================================
熱バランス
========================================================================================================================

------------------------------------------------------------------------------------------------------------------------
1. 境界表面における熱収支
------------------------------------------------------------------------------------------------------------------------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1) 表面温度
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ステップ |n+1| における境界 |j| の表面温度 :math:`\theta_{s,j,n+1}` は式(1)～(3)により表される。

.. math::
    :nowrap:

    \begin{align*}
        \theta_{s,j,n+1}
        = \phi_{a0,j} \cdot q_{s,j,n+1} + \sum_{m=1}^{M}{\theta'_{s,a,j,m,n+1}}
        + \phi_{t0,j} \cdot \theta_{s,rear,j,n+1} + \sum_{m=1}^{M}{\theta'_{s,t,j,m,n+1}}
        \tag{1}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \theta'_{s,a,j,m,n+1} = \phi_{a1,j,m} \cdot q_{s,j,n} + r_{j,m} \cdot \theta'_{s,a,j,m,n}
        \tag{2}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \theta'_{s,t,j,m,n+1} = \phi_{t1,j,m} \cdot \theta_{s,rear,j,n} + r_{j,m} \cdot \theta'_{s,t,j,m,n}
        \tag{3}
    \end{align*}

ここで、

:math:`\theta_{s,j,n+1}` : ステップ |n+1| における境界 |j| の表面温度, ℃

:math:`\phi_{a0,j}` : 境界 |j| の吸熱応答係数の初項, |m2| K / W

:math:`q_{s,j,n}` : ステップ |n| における境界 |j| の表面熱流（壁体吸熱を正とする）, W / |m2|

:math:`q_{s,j,n+1}` : ステップ |n+1| における境界 |j| の表面熱流（壁体吸熱を正とする）, W / |m2|

:math:`\phi_{t0,j}` : 境界 |j| の貫流応答係数の初項, -

:math:`\theta_{s,rear,j,n}` : ステップ |n| における境界 |j| の裏面温度, ℃

:math:`\theta_{s,rear,j,n+1}` : ステップ |n+1| における境界 |j| の裏面温度, ℃

:math:`\theta'_{s,a,j,m,n}` : ステップ |n| における境界 |j| の項別公比法の指数項 |m| の吸熱応答の項別成分, ℃

:math:`\theta'_{s,a,j,m,n+1}` : ステップ |n+1| における境界 |j| の項別公比法の指数項 |m| の吸熱応答の項別成分, ℃

:math:`\theta'_{s,t,j,m,n}` : ステップ |n| における境界 |j| の項別公比法の指数項 |m| の貫流応答の項別成分, ℃

:math:`\theta'_{s,t,j,m,n+1}` : ステップ |n+1| における境界 |j| の項別公比法の指数項 |m| の貫流応答の項別成分, ℃

:math:`\phi_{a1,j,m}` : 境界 |j| の項別公比法の指数項 |m| の吸熱応答係数, |m2| K / W

:math:`\phi_{t1,j,m}` : 境界 |j| の項別公比法の指数項 |m| の貫流応答係数, -

:math:`r_{j,m}` : 境界 |j| の項別公比法の指数項 |m| の公比, -

である。 :math:`M` は項別公比法の指数項の数である。

これらの式を境界 :math:`0` ～ :math:`J-1` でベクトル表記をすると、式(4)～(6)となる。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{s,n+1} = \pmb{\phi}_{a0} \cdot \pmb{q}_{s,n+1} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}}
        + \pmb{\phi}_{t0} \cdot \pmb{\theta}_{s,rear,n+1} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        \tag{4}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}'_{s,a,m,n+1} = \pmb{\phi}_{a1,m} \cdot \pmb{q}_{s,n} + \pmb{r}_{m} \cdot \pmb{\theta}'_{s,a,m,n}
        \tag{5}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}'_{s,t,m,n+1}
        = \pmb{\phi}_{t1,m} \cdot \pmb{\theta}_{s,rear,n} + \pmb{r}_{m} \cdot \pmb{\theta}'_{s,t,m,n}
        \tag{6}
    \end{align*}

ここで、

:math:`\pmb{\theta}_{s,n}` : :math:`\theta_{s,j,n}` を要素にもつ :math:`J \times 1` の縦行列, ℃

:math:`\pmb{\phi}_{a0}` : :math:`\phi_{a0,j}` を要素にもつ :math:`J \times J` の対角化行列, |m2| K / W

:math:`\pmb{\phi}_{t0}` : :math:`\phi_{t0,j}` を要素にもつ :math:`J \times J` の対角化行列, -

:math:`\pmb{q}_{s,n}` : :math:`q_{s,j,n}` を要素にもつ :math:`J \times 1` の縦行列, W / |m2|

:math:`\pmb{q}_{s,n+1}` : :math:`q_{s,j,n+1}` を要素にもつ :math:`J \times 1` の縦行列, W / |m2|

:math:`\pmb{\theta}_{s,rear,n}` : :math:`\theta_{s,rear,j,n}` を要素にもつ :math:`J \times 1` の縦行列, ℃

:math:`\pmb{\theta}_{s,rear,n+1}` : :math:`\theta_{s,rear,j,n+1}` を要素にもつ :math:`J \times 1` の縦行列, ℃

:math:`\pmb{\theta}'_{s,a,m,n}` : :math:`\theta'_{s,a,j,m,n}` を要素にもつ :math:`J \times 1` の縦行列, ℃

:math:`\pmb{\theta}'_{s,a,m,n+1}` : :math:`\theta'_{s,a,j,m,n+1}` を要素にもつ :math:`J \times 1` の縦行列, ℃

:math:`\pmb{\theta}'_{s,t,m,n}` : :math:`\theta'_{s,t,j,m,n}` を要素にもつ :math:`J \times 1` の縦行列, ℃

:math:`\pmb{\theta}'_{s,t,m,n+1}` : :math:`\theta'_{s,t,j,m,n+1}` を要素にもつ :math:`J \times 1` の縦行列, ℃

:math:`\pmb{\phi}_{a1,m}` : :math:`\phi_{a1,j,m}` を要素にもつ :math:`J \times J` の対角化行列, |m2| K / W

:math:`\pmb{\phi}_{t1,m}` : :math:`\phi_{t1,j,m}` を要素にもつ :math:`J \times J` の対角化行列, -

:math:`\pmb{r}_{m}` : :math:`r_{j,m}` を要素にもつ :math:`J \times J` の対角化行列, -

である。

なお、境界の吸熱応答係数の初項 :math:`\pmb{\phi}_{a0}` など、室温や熱流にかける変数については、
本来であれば :math:`J \times 1` の1次元のベクトルであるが、
後のベクトル計算の記述性・操作性を考え、予め対角化した行列として表現している。
なお、室温や日射量等の状態量を表す変数は、対角化せずに、 :math:`J \times 1` の行列で表す。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2) 表面熱流
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ステップ |n| における境界 |j| の表面熱流 :math:`q_{s,j,n}` は式(7)により表される。

.. math::
    :nowrap:

    \begin{align*}
        q_{s,j,n} = h_{s,i,j} \cdot ( \theta_{er,j,n} - \theta_{s,j,n} )
        \tag{7}
    \end{align*}

ここで、

:math:`h_{s,i,j}` : 境界 |j| の室内側総合熱伝達率, W / |m2| K

:math:`\theta_{er,j,n}` : ステップ |n| における境界 |j| の等価室温, ℃

である。

これらの式を境界 :math:`0` ～ :math:`J-1` でベクトル表記をすると、式(8)となる。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{q}_{s,n} = \pmb{h}_{s,i} \cdot ( \pmb{\theta}_{er,n} - \pmb{\theta}_{s,n} )
        \tag{8}
    \end{align*}

ここで、

:math:`\pmb{h}_{s,i}` : :math:`h_{s,i,j}` を要素にもつ :math:`J \times J` の対角化行列, W / |m2| K

:math:`\pmb{\theta}_{er,n}` : :math:`\theta_{er,j,m}` を要素にもつ :math:`J \times 1` の縦行列, ℃

である。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3) 等価室温
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

境界の表面における熱流を対流・放射・日射熱取得・放射空調からの熱取得に分けて記述すると次式となる。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            q_{s,j,n}
            &= h_{s,c,j} \cdot (\theta_{r,j,n} - \theta_{s,j,n})
            + h_{s,r,j} \cdot (\theta_{MRT,j,n} - \theta_{s,j,n}) \\
            &+ q_{s,sol,j,n}
            + \frac{ f_{flr,j,i} \cdot L_{RS,i,n} \cdot (1 - \beta_i) }{A_{s,j}}
        \end{split}
        \tag{9}
    \end{align*}

ここで、

:math:`h_{s,c,j}` : 境界 |j| の室内側対流熱伝達率, W / |m2| K

:math:`h_{s,r,j}` : 境界 |j| の室内側放射熱伝達率, W / |m2| K

:math:`\theta_{r,j,n}` : ステップ |n| における境界 |j| が接する室の空気温度, ℃

:math:`\theta_{MRT_j,n}` : ステップ |n| における境界 |j| の平均放射温度, ℃

:math:`q_{s,sol,j,n}` : ステップ |n| における境界 |j| の透過日射吸収熱量, W / |m2|

:math:`f_{flr,j,i}` : 室 |i| に設置された放射空調の放熱量のうち放射成分に対する境界 |j| の室内側表面の吸収比率, -

:math:`L_{RS,i,n}` : ステップ |n| における室 |i| に設置された放射空調の放熱量, W

:math:`\beta_{i}` : 室 |i| に設置された放射空調の対流成分比率, -

:math:`A_{s,j}` : 境界 |j| の面積, |m2|

である。この境界表面における熱流は式(7)（再掲）のように表されるため、

.. math::
    :nowrap:

    \begin{align*}
        q_{s,j,n} = h_{s,i,j} \cdot ( \theta_{er,j,n} - \theta_{s,j,n} )
        \tag{7}
    \end{align*}

ステップ |n| における境界 |j| の等価室温 :math:`\theta_{s,ei,j,n}` は式(10)のように表される。

.. math::
    :nowrap:

    \begin{align*}
        \theta_{er,j,n}
        = \frac{h_{s,c,j}}{h_{s,i,j}} \cdot \theta_{r,j,n}
        + \frac{h_{s,r,j}}{h_{s,i,j}} \cdot \theta{MRT_j,n}
        + \frac{q_{s,sol,j,n}}{h_{s,i,j}}
        + \frac{f_{flr,j,i} \cdot L_{RS,i,n} \cdot (1 - \beta_i) }{A_{s,j} \cdot h_{s,i,j}}
        \tag{10}
    \end{align*}

これらの式を境界 :math:`0` ～ :math:`J-1` でベクトル表記をすると、式(11)となる。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{er,n} = \pmb{h}_{s,i}^{-1} \cdot
        ( \pmb{h}_{s,c} \cdot \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n} + \pmb{h}_{s,r} \cdot \pmb{\theta}_{MRT,n}
        + \pmb{q}_{s,sol,n} + \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta}) \cdot \pmb{r}_{RS,n} )
        \tag{11}
    \end{align*}

ここで、

:math:`\pmb{h}_{s,c}` : :math:`h_{s,c,j}` を要素にもつ :math:`J \times J` の対角化行列, W / |m2| K

:math:`\pmb{h}_{s,r}` : :math:`h_{s,r,j}` を要素にもつ :math:`J \times J` の対角化行列, W / |m2| K

:math:`\pmb{h}_{s,i}` : :math:`h_{s,i,j}` を要素にもつ :math:`J \times J` の対角化行列, W / |m2| K

:math:`\pmb{p}_{ji}` : :math:`p_{j,i}` を要素にもつ :math:`J \times I` の行列

:math:`\pmb{\theta}_{r,n}` : :math:`\theta'_{r,i,n}` を要素にもつ :math:`I \times 1` の縦行列, ℃

:math:`\pmb{\theta}_{MRT,n}` : :math:`\theta_{MRT,j,n}` を要素にもつ :math:`J \times 1` の縦行列, ℃

:math:`\pmb{q}_{s,sol,n}` : :math:`q_{s,sol,j}` を要素にもつ :math:`J \times 1` の縦行列, W / |m2|

:math:`\pmb{f}_{flr}` : :math:`f_{flr,j,i}` を要素にもつ :math:`J \times I` の行列, -

:math:`\pmb{L}_{RS,n}` : :math:`L_{RS,i,n}` を要素にもつ :math:`I \times 1` の縦行列, W

:math:`\pmb{\beta}` : :math:`\beta_{i}` を要素にもつ :math:`I \times I` の対角化行列, -

:math:`\pmb{A}_{s}` : :math:`A_{s,i}` を要素にもつ :math:`I \times I` の対角化行列, |m2|

である。
ここで、ステップ |n| における境界 |j| が接する室の空気温度は、

.. math::
    :nowrap:

    \begin{align*}
        \begin{pmatrix}
        \theta_{r,0,n} \\
        \vdots \\
        \theta_{r,J-1,n}
        \end{pmatrix} =
        \begin{pmatrix}
        p_{0,0} & \ldots & p_{0,I-1} \\
        \vdots & \ddots & \vdots \\
        p_{J-1,0} & \ldots & p_{J-1,I-1}
        \end{pmatrix} \cdot
        \begin{pmatrix}
        \theta_{r,0} \\
        \vdots \\
        \theta_{r,I-1}
        \end{pmatrix} =
        \pmb{p}_{ji} \cdot \pmb{\theta}_r
    \end{align*}

の関係を用いて、 :math:`I \times 1` の要素を :math:`J \times 1` の要素に変換している。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
4) 裏面温度
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

裏面温度は、境界の種類によって、

- 外気温度（相当外気温度）の場合
- 外気温度（相当外気温度）と室内温度を按分する場合（温度差係数が1ではない場合）
- 隣室の温度（裏面の等価温度）の場合

が考えられ、一般化して式(12)のように定義する。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \theta_{s,rear,j,n}
            &=
            \begin{pmatrix}
                k_{s,er,j,0} & \ldots & k_{s,er,j,J-1}
            \end{pmatrix} \cdot
            \begin{pmatrix}
                \theta_{er,0,n} \\
                \vdots \\
                \theta_{er,J-1,n}
            \end{pmatrix} \\
            &+
            \begin{pmatrix}
                k_{s,r,j,0} & \ldots & k_{s,r,j,I-1}
            \end{pmatrix} \cdot
            \begin{pmatrix}
                \theta_{r,0,n} \\
                \vdots \\
                \theta_{r,I-1,n}
            \end{pmatrix} \\
            &+ k_{s,eo,j} \cdot \theta_{eo,j,n}
        \end{split}
        \tag{12}
    \end{align*}

ここで、

:math:`k_{s,er,j,j^*}` : 境界 |j| の裏面温度に境界　|j*| の等価温度が与える影響

:math:`k_{s,eo,j}` : 境界 |j| の裏面温度に屋外側等価温度が与える影響

:math:`k_{s,r,j,i}` : 境界 |j| の裏面温度に室 |i| の空気温度が与える影響

:math:`\theta_{eo,j,n}` : ステップ |n| における境界 |j| の屋外側等価温度, ℃

である。

例えば、外気温度の場合、
:math:`k_{s,er,j,0}` ～ :math:`k_{s,er,j,J-1}` は :math:`0.0`、
:math:`k_{s,r,j,0}` ～ :math:`k_{s,r,j,I-1}` は :math:`0.0`、
:math:`k_{s,eo,j}` は :math:`1.0` である。

外気温度と室内温度を按分する場合の例として例えば床下の場合は温度差係数 :math:`0.7` が採用されるが、
その場合の床下に面する境界の室（表側：裏面側ではない）の空気温度を |i*| とすると、
:math:`k_{s,er,j,0}` ～ :math:`k_{s,er,j,J-1}` は :math:`0.0`、
:math:`k_{s,r,j,i*}` は :math:`0.3` 、その他の :math:`k_{s,r,j,i}` は0.0、
:math:`k_{s,eo,j}` は :math:`0.7` である。

間仕切り等、裏面が室の場合、
:math:`k_{s,er,j,0}` ～ :math:`k_{s,er,j,J-1}` のどれかが :math:`1.0`,
:math:`k_{s,r,j,0}` ～ :math:`k_{s,r,j,I-1}` は :math:`0.0`、
:math:`k_{s,eo,j}` は :math:`0.0` である。

これらの式を境界 :math:`0` ～ :math:`J-1` および :math:`0` ～ :math:`I-1` でベクトル表記をすると、次式となる。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{s,rear,n}
        = \pmb{k}_{s,er} \cdot \pmb{\theta}_{er,n}
        + \pmb{k}_{s,r} \cdot \pmb{\theta}_{r,n}
        + \pmb{k}_{s,eo} \cdot \pmb{\theta}_{eo,n}
        \tag{13}
    \end{align*}

ここで、

:math:`\pmb{k}_{s,er}` : :math:`k_{s,er,j,j^*}` を要素にもつ :math:`J \times J` の行列

:math:`\pmb{k}_{s,eo}` : :math:`k_{s,eo,j}` を要素にもつ :math:`J \times I` の縦行列

:math:`\pmb{k}_{s,r}` : :math:`k_{s,r,j,i}` を要素にもつ :math:`J \times I` の行列

:math:`\pmb{\theta}_{eo,n}` : :math:`\theta_{eo,j,n}` を要素にもつ :math:`J \times 1` の縦行列

である。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
5) 平均放射温度と放射熱伝達率
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ステップ |n| における境界 |j| の等価室温 :math:`\theta_{er,j,n}` を求めるにあたり、放射のやりとりは、

.. math::
    :nowrap:

    \begin{align*}
        h_{s,r,j} \cdot \theta_{MRT_j,n}
    \end{align*}

で表されるが、ここで、 :math:`\theta_{MRT_j,n}` を室 |i| の微小球の温度で代表させると、平均放射温度 :math:`MRT` は室 |i| ごとに定められ、

.. math::
    :nowrap:

    \begin{align*}
        \theta_{MRT_i,n} = \sum_{j=0}^{J-1}{f_{mrt,i,j}} \cdot \theta_{s,j,n}
        \tag{14}
    \end{align*}

となる。ここで、

:math:`f_{mrt,i,j}` : 境界 |j| の室 |i| の微小球の放射温度に対する表面温度の重み, -

である。放射熱伝達率についても微小球に対するものとして再定義される。この放射のやりとりをベクトル表記すると、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt} \cdot \pmb{\theta}_{s,n}
    \end{align*}

となる。ここで、

:math:`\pmb{f}_{mrt}` : :math:`f_{mrt,i,j}` を要素にもつ :math:`I \times J` の行列

である。
この関係を式(11)に代入すると、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \pmb{\theta}_{er,n}
            &= \pmb{h}_{s,i}^{-1} \cdot
            ( \pmb{h}_{s,c} \cdot \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n}
            + \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt} \cdot \pmb{\theta}_{s,n} \\
            &+ \pmb{q}_{s,sol,n}
            + \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta}) \cdot \pmb{L}_{RS,n}
            )
        \end{split}
        \tag{15}
    \end{align*}

となる。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
6) 表面温度の関係式の整理
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

これまで整理した式、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{s,n+1} = \pmb{\phi}_{a0} \cdot \pmb{q}_{s,n+1} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}}
        + \pmb{\phi}_{t0} \cdot \pmb{\theta}_{s,rear,n+1} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        \tag{4}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{q}_{s,n} = \pmb{h}_{s,i} \cdot ( \pmb{\theta}_{er,n} - \pmb{\theta}_{s,n} )
        \tag{8}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{s,rear,n}
        = \pmb{k}_{s,er} \cdot \pmb{\theta}_{er,n}
        + \pmb{k}_{s,r} \cdot \pmb{\theta}_{r,n}
        + \pmb{k}_{s,eo} \cdot \pmb{\theta}_{eo,n}
        \tag{13}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \pmb{\theta}_{er,n}
            &= \pmb{h}_{s,i}^{-1} \cdot
            ( \pmb{h}_{s,c} \cdot \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n}
            + \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt} \cdot \pmb{\theta}_{s,n} \\
            &+ \pmb{q}_{s,sol,n}
            + \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta}) \cdot \pmb{L}_{RS,n}
            )
        \end{split}
        \tag{15}
    \end{align*}

について、順次代入すると、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \pmb{\theta}_{s,n+1}
            &= \pmb{\phi}_{a0} \cdot \pmb{q}_{s,n+1}
            + \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}}
            + \pmb{\phi}_{t0} \cdot \pmb{\theta}_{s,rear,n+1}
            + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}} \\
            &= \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i} \cdot ( \pmb{\theta}_{er,n+1} - \pmb{\theta}_{s,n+1} ) \\
            &+ \pmb{\phi}_{t0} \cdot (\pmb{k}_{s,er} \cdot \pmb{\theta}_{er,n+1} + \pmb{k}_{s,r} \cdot \pmb{\theta}_{r,n+1} + \pmb{k}_{s,eo} \cdot \pmb{\theta}_{eo,n+1}) \\
            &+ \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}} \\
            &= \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i} \cdot \pmb{h}_{s,i}^{-1} \cdot (\pmb{h}_{s,c} \cdot \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n+1} + \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt} \cdot \pmb{\theta}_{s,n+1} \\
            &+ \pmb{q}_{s,sol,n+1} + \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta}) \cdot \pmb{L}_{RS,n+1}) \\
            &- \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i} \cdot \pmb{\theta}_{s,n+1} \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot (\pmb{h}_{s,c} \cdot \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n+1} + \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt} \cdot \pmb{\theta}_{s,n+1} \\
            &+ \pmb{q}_{s,sol,n+1} + \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta}) \cdot \pmb{L}_{RS,n+1}) \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,r} \cdot \pmb{\theta}_{r,n+1} \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,eo} \cdot \pmb{\theta}_{eo,n+1} \\
            &+ \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}} \\
            &= \pmb{\phi}_{a0} \cdot \pmb{h}_{s,c} \cdot \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n+1} \\
            &+ \pmb{\phi}_{a0} \cdot \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt} \cdot \pmb{\theta}_{s,n+1} \\
            &+ \pmb{\phi}_{a0} \cdot \pmb{q}_{s,sol,n+1} \\
            &+ \pmb{\phi}_{a0} \cdot \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta}) \cdot \pmb{L}_{RS,n+1} \\
            &- \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i} \cdot \pmb{\theta}_{s,n+1} \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{h}_{s,c} \cdot \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n+1} \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt} \cdot \pmb{\theta}_{s,n+1} \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{q}_{s,sol,n+1} \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta}) \cdot \pmb{L}_{RS,n+1} \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,r} \cdot \pmb{\theta}_{r,n+1} \\
            &+ \pmb{\phi}_{t0} \cdot \pmb{k}_{s,eo} \cdot \pmb{\theta}_{eo,n+1} \\
            &+ \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        \end{split}
        \tag{16}
    \end{align*}

となる。

:math:`\pmb{\theta}_{s,n+1}` に関係する項を左辺に移動させると、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            & (\pmb{I}
            - \pmb{\phi}_{a0} \cdot \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt}
            + \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i}
            - \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt}
            ) \cdot \pmb{\theta}_{s,n+1} \\
            &= (\pmb{\phi}_{a0} \cdot \pmb{h}_{s,c} \cdot \pmb{p}_{ji}
            + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{h}_{s,c} \cdot \pmb{p}_{ji}
            + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,r}
            ) \cdot \pmb{\theta}_{r,n+1} \\
            &+ \pmb{\phi}_{a0} \cdot \pmb{q}_{s,sol,n+1}
            + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{q}_{s,sol,n+1}
            + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,eo} \cdot \pmb{theta}_{eo,n+1} \\
            &+ (\pmb{\phi}_{a0} \cdot \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta})
            + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{A}_{s}^{-1} \cdot \pmb{f}_{flr} \cdot (\pmb{I} - \pmb{\beta})
            ) \cdot \pmb{L}_{RS,n+1} \\
            &+ \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        \end{split}
        \tag{17}
    \end{align*}

となる。

ここで、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{AX}
        = \pmb{I}
        + \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i}
        - \pmb{\phi}_{a0} \cdot \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt}
        - \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{h}_{s,r} \cdot \pmb{p}_{ji} \cdot \pmb{f}_{mrt}
        \tag{18}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{FIA} = (\pmb{\phi}_{a0} \cdot \pmb{h}_{s,c} \cdot \pmb{p}_{ji}
        + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{h}_{s,c} \cdot \pmb{p}_{ji}
        + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,r}
        \tag{19}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{CRX,n+1}
        = \pmb{\phi}_{a0} \cdot \pmb{q}_{s,sol,n+1}
        + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{h}_{s,i}^{-1} \cdot \pmb{q}_{s,sol,n+1}
        + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,eo} \cdot \theta_{eo,eqv,n+1}
        \tag{20}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{FLB} = (
        \pmb{\phi}_{a0} \cdot \pmb{A}_{s}^{-1}
        + \pmb{\phi}_{t0} \cdot \pmb{k}_{s,er} \cdot \pmb{A}_{s}^{-1} \cdot \pmb{h}_{s,i}^{-1}
        ) \cdot (\pmb{I} - \pmb{\beta}) \cdot \pmb{f}_{flr}
        \tag{21}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{CVL,n+1} = \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        \tag{22}
    \end{align*}

とおくと、式(17)は次式のように表すことができる。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{AX} \cdot \pmb{\theta}_{s,n+1}
        = \pmb{f}_{FIA} \cdot \pmb{\theta}_{r,n+1} + \pmb{f}_{CRX,n+1} + \pmb{f}_{FLB} \cdot \pmb{L}_{RS,n+1} + \pmb{f}_{CVL,n+1}
        \tag{23}
    \end{align*}

この式の各項に左から :math:`\pmb{f}_{AX}` の逆行列をかけて、次のように式変形する。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \pmb{\theta}_{s,n+1}
            &= \pmb{f}_{AX}^{-1} \cdot (
            \pmb{f}_{FIA} \cdot \pmb{\theta}_{r,n+1} + \pmb{f}_{CRX,n+1}
            + \pmb{f}_{FLB} \cdot \pmb{L}_{RS,n+1} + \pmb{f}_{CVL,n+1} ) \\
            &= \pmb{f}_{WSR} \cdot \pmb{\theta}_{r,n+1}
            + \pmb{f}_{WSC,n+1}
            + \pmb{f}_{WSB} \cdot \pmb{L}_{RS,n+1}
            + \pmb{f}_{WSV,n+1}
        \end{split}
        \tag{24}
    \end{align*}

ここで、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{WSR} = \pmb{f}_{AX}^{-1} \cdot \pmb{f}_{FIA}
        \tag{25}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{WSC,n+1} = \pmb{f}_{AX}^{-1} \cdot \pmb{f}_{CRX,n+1}
        \tag{26}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{WSB} = \pmb{f}_{AX}^{-1} \cdot \pmb{f}_{FLB}
        \tag{27}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{WSV,n+1} = \pmb{f}_{AX}^{-1} \cdot \pmb{f}_{CVL,n+1}
        \tag{28}
    \end{align*}

とした。

------------------------------------------------------------------------------------------------------------------------
2. 室空気の熱収支
------------------------------------------------------------------------------------------------------------------------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1) 室空気の熱収支
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

室の熱収支は次のように表される。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            C_{rm,i} \cdot \frac{d \theta_{r,i,n}}{d t}
            &= \sum_{j \in \pmb{J}_i}{h_{s,c,j} \cdot A_{s,j} \cdot ( \theta_{s,j,n} - \theta_{r,j,n} )} \\
            &+ c_a \cdot \rho_a \cdot V_{vent,out,i,n} \cdot ( \theta_{o,n} - \theta_{r,i,n} )
            + c_a \cdot \rho_a \cdot \sum_{i^*}^{I}{V_{vent,int,i,i^*,n} \cdot \theta_{i^*}} \\
            &+ H_{i,n} + (L_{CS,i,n} + \beta_i \cdot L_{RS,i,n}) \\
            &+ G_{sh,frt,i} \cdot ( \theta_{frt,i,n} - \theta_{r,i,n} ) \\
        \end{split}
        \tag{29}
    \end{align*}

ここで、

:math:`C_{rm,i}` : 室 |i| の空気の熱容量, J / K

:math:`t` : 時刻, s

:math:`c_a` : 空気の比熱, J / kg K

:math:`\rho_a` : 空気の密度, kg / |m3|

:math:`V_{vent,out,i,n}` : ステップ |n| における室 |i| の換気・すきま風・自然風の利用による外気の流入量, |m3| / s

:math:`V_{vent,int,i,i^*,n}` : ステップ |n| における室 |i*| から室 |i| への室間の空気移動量, |m3| / s

:math:`H_{i,n}` : ステップ |n| における室 |i| の室内発熱, W

:math:`L_{CS,i,n}` : ステップ |n| における室 |i| に設置された対流暖房の放熱量, W

:math:`G_{sh,frt,i}` : 室 |i| の備品等と空気間の熱コンダクタンス, W/K

:math:`\theta_{fun,i,n}` : ステップ |n| における室 |i| に設置された備品等の温度, ℃

ここで、 |i| は流入先の室番号を表し、 |i*| は流出元の室番号を表す。

なお、変数 :math:`V_{vent,int,i,i^*}` について、
例えば、 :math:`V_{vent,int,2,0}` は室 :math:`2` から室 :math:`0` への空気流入量を表すとともに、
:math:`V_{vent,int,0,0}` は室 :math:`0` から他室への空気流出量を表すこととする。
流入する空気の合計と流出する空気の合計は一致することから、

.. math::
    :nowrap:

        \begin{align*}
            V_{vent,int,i,i} = - \sum_{i^*, i^* \ne i}{V_{vent,int,i,i^*}}
        \end{align*}

が成り立つ。

式(29)を室 :math:`0` ～ :math:`I-1` でベクトル表記をすると、式(30)となる。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \pmb{C}_{rm} \cdot \frac{d \pmb{\theta}_{r,n}}{d t}
            & = \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot (\pmb{\theta}_{s,n} - \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n}) \\
            & + c_a \cdot \rho_a \cdot \pmb{V}_{vent,out,n} \cdot (\pmb{\theta}_{o,n} - \pmb{\theta}_{r,n})
            + c_a \cdot \rho_a \cdot \pmb{V}_{vent,int,n} \cdot \pmb{\theta}_{r,n} \\
            & + \pmb{H}_n
            + (\pmb{L}_{CS,n} + \pmb{\beta} \cdot \pmb{L}_{RS,n})
            + \pmb{G}_{sh,frt} \cdot (\pmb{\theta}_{frt,n} - \pmb{\theta}_{r,n})
        \end{split}
        \tag{30}
    \end{align*}

ここで、

:math:`\pmb{C}_{rm}` : :math:`C_{rm,i}` を要素にもつ :math:`I \times I` の対角化行列, J / K

:math:`\pmb{V}_{vent,out,n}` : :math:`V_{vent,out,i,n}` を要素にもつ :math:`I \times I` の対角化行列, |m3| / s

:math:`\pmb{V}_{vent,int,n}` : :math:`V_{vent,int,i,i^*}` を要素にもつ :math:`I \times I` の行列, |m3| / s

:math:`\pmb{H}_n` : :math:`H_{i,n}` を要素にもつ :math:`I \times 1` の縦行列, W

:math:`\pmb{L}_{CS,n}` : :math:`L_{CS,i,n}` を要素にもつ :math:`I \times 1` の縦行列, W

:math:`\pmb{G}_{sh,frt}` : :math:`G_{sh,frt,i}` を要素にもつ :math:`I \times I` の対角化行列, W/K

:math:`\pmb{\theta}_{fun,n}` : :math:`\theta_{fun,i,n}` を要素にもつ :math:`I \times 1` の縦行列, ℃

である。ここで、室 |i| が接する境界表面の熱流を仮に :math:`q_{s,bdr,j}` とし、それらの室 |i| における合計を :math:`q_{s,rm,i}` とすると、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{q}_{s,rm} =
        \begin{pmatrix}
        q_{s,rm,0} \\
        \vdots \\
        q_{s,rm,I-1}
        \end{pmatrix} =
        \begin{pmatrix}
        p_{0,0} & \ldots & p_{0,J-1} \\
        \vdots & \ddots & \vdots \\
        p_{I-1,0} & \ldots & p_{I-1,J-1}
        \end{pmatrix} \cdot
        \begin{pmatrix}
        q_{s,bdr,0} \\
        \vdots \\
        q_{s,bdr,J-1}
        \end{pmatrix} =
        \pmb{p}_{ji}^T \cdot \pmb{q}_{s,bdr}
    \end{align*}

の関係を用いて、 :math:`J \times 1` の要素を :math:`I \times 1` の要素に変換している。


両辺をステップ |n| から |n+1| まで積分すると左辺は、

.. math::
    :nowrap:

    \begin{align*}
        \left. \frac{d \pmb{\theta}_r}{dt} \right |_n
        = \frac{\pmb{\theta}_{r,n} - \pmb{\theta}_{r,n-1}}{\Delta t}
    \end{align*}

のようになり、右辺は　|n| から |n+1| までの平均値（本来であれば積算値であるが、
全体を :math:`\Delta n` で除しているので平均値）となるが、
平均値が計算できない温度の項についてはステップ |n+1| の瞬時値で代表させることとする（後退差分）。
換気量・放熱量については |n| から |n+1| までの平均値として定義し、
瞬時値と区別するために以後の式展開では記号の上側にハットを付すこととする。

室の熱収支は式(31)となる。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            &\pmb{C}_{rm} \frac{\pmb{\theta}_{r,n+1} - \pmb{\theta}_{r,n}}{\Delta t} \\
            & = \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot (\pmb{\theta}_{s,n+1} - \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n+1}) \\
            & + c_a \cdot \rho_a \cdot \hat{\pmb{V}}_{vent,out,n} \cdot (\pmb{\theta}_{o,n+1} - \pmb{\theta}_{r,n+1})
            + c_a \cdot \rho_a \cdot \hat{\pmb{V}}_{vent,int,n} \cdot \pmb{\theta}_{r,n+1} \\
            & + \hat{\pmb{H}}_n
            + ( \hat{\pmb{L}}_{CS,n} + \pmb{\beta} \cdot \hat{\pmb{L}}_{RS,n} )
            + \pmb{G}_{sh,frt} \cdot (\pmb{\theta}_{frt,n+1} - \pmb{\theta}_{r,n+1})
        \end{split}
        \tag{31}
    \end{align*}

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2) 室の家具と空間との熱収支
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

家具の熱収支は次式で表される。

.. math::
    :nowrap:

    \begin{align*}
        C_{sh,frt,i} \cdot \frac{d \theta_{frt,i,n}}{d t}
        = G_{sh,frt,i} \cdot (\theta_{r,i,n} - \theta_{frt,i,n}) + Q_{sol,frt,i,n}
        \tag{32}
    \end{align*}

ここで、

:math:`C_{sh,frt,i}` : 室 |i| に設置された家具の熱容量, J / K

:math:`Q_{sol,frt,i,n}` : ステップ |n| における室 |i| に設置された家具による透過日射吸収熱量, W

である。

式(32)を室 :math:`0` ～ :math:`I-1` でベクトル表記をすると、式(33)となる。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{C}_{sh,frt} \cdot \frac{d \pmb{\theta}_{frt,n}}{d t}
        = \pmb{G}_{sh,frt} \cdot (\pmb{\theta}_{r,n} - \pmb{\theta}_{frt,n}) + \pmb{Q}_{sol,frt,n}
        \tag{33}
    \end{align*}

ここで、

:math:`\pmb{C}_{sh,frt}` : :math:`C_{sh,frt,i}` を要素にもつ :math:`I \times I` の対角化行列, J / K

:math:`\pmb{Q}_{sol,frt,n}` : :math:`Q_{sol,frt,i}` を要素にもつ :math:`I \times 1` の縦行列, W

である。

この式を差分で表すと次式となる。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{C}_{sh,frt} \cdot \frac{\pmb{\theta}_{frt,n+1} - \pmb{\theta}_{frt,n}}{\Delta t}
        = \pmb{G}_{sh,frt} \cdot (\pmb{\theta}_{r,n+1} - \pmb{\theta}_{frt,n+1}) + \hat{\pmb{Q}}_{sol,frt,n}
        \tag{34}
    \end{align*}

この式を :math:`\pmb{\theta}_{frt,n+1}` について解くと、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            &\pmb{\theta}_{frt,n+1} \\
            &= (\pmb{C}_{sh,frt} + \Delta t \cdot \pmb{G}_{sh,frt})^{-1}
            \cdot
            (
            \pmb{C}_{sh,frt} \cdot \pmb{\theta}_{frt,n}
            + \Delta t \cdot \pmb{G}_{sh,frt} \cdot \pmb{\theta}_{r,n+1}
            + \Delta t \cdot \hat{\pmb{Q}}_{sol,frt,n+1}
            )
        \end{split}
        \tag{35}
    \end{align*}

となる。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3) 関係式の整理
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

式(35)と表面温度に関する関係式(24)を、式(31)に代入すると、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            &\pmb{C}_{rm} \frac{\pmb{\theta}_{r,n+1} - \pmb{\theta}_{r,n}}{\Delta t} \\
            &= \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot
            (
            \pmb{f}_{WSR} \cdot \pmb{\theta}_{r,n+1}
            + \pmb{f}_{WSC,n+1}
            + \pmb{f}_{WSB} \cdot \pmb{L}_{RS,n+1} \\
            &+ \pmb{f}_{WSV,n+1}
            - \pmb{p}_{ji} \cdot \pmb{\theta}_{r,n+1}
            ) \\
            &+ c_a \cdot \rho_a \cdot \hat{\pmb{V}}_{vent,out,n} \cdot (\pmb{\theta}_{o,n+1} - \pmb{\theta}_{r,n+1}) \\
            &+ c_a \cdot \rho_a \cdot \hat{\pmb{V}}_{vent,int,n} \cdot \pmb{\theta}_{r,n+1} \\
            &+ \hat{\pmb{H}}_n + ( \hat{\pmb{L}}_{CS,n} + \pmb{\beta} \cdot \hat{\pmb{L}}_{RS,n} ) \\
            &+ \pmb{G}_{sh,frt} \cdot ( (\pmb{C}_{sh,frt} + \Delta t \cdot \pmb{G}_{sh,frt})^{-1} \\
            &\cdot
            (
            \pmb{C}_{sh,frt} \cdot \pmb{\theta}_{frt,n}
            + \Delta t \cdot \pmb{G}_{sh,frt} \cdot \pmb{\theta}_{r,n+1}
            + \Delta t \cdot \hat{\pmb{Q}}_{sol,frt,n+1}
            ) - \pmb{\theta}_{r,n+1})
        \end{split}
        \tag{36}
    \end{align*}

となる。

表面温度は応答係数法を用いて計算しているため、　:math:`\pmb{L}_{RS,n+1}` はステップ |n+1| における瞬時値である。
一方で、設備による放熱量等の値はステップ |n| からステップ |n+1| までの積算値である。
ここでは、 :math:`\pmb{L}_{RS,n+1}` を :math:`\hat{\pmb{L}}_{RS,n}` で代表させ、
:math:`\pmb{\theta}_{r,n+1}` を左辺に移動させ、
右辺は、:math:`\hat{\pmb{L}}_{RS,n}` 及び :math:`\hat{\pmb{L}}_{CS,n}` でまとめると、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            & \pmb{C}_{rm} \cdot \frac{1}{\Delta t} \cdot \pmb{\theta}_{r,n+1} \\
            &+ \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot (\pmb{p}_{ji} - \pmb{f}_{WSR}) \cdot \pmb{\theta}_{r,n+1} \\
            & + c_a \cdot \rho_a \cdot \hat{\pmb{V}}_{vent,out,n} \cdot \pmb{\theta}_{r,n+1}
            - c_a \cdot \rho_a \cdot \hat{\pmb{V}}_{vent,int,n} \cdot \pmb{\theta}_{r,n+1} \\
            &+ \pmb{G}_{sh,frt} \cdot ( \pmb{C}_{sh,frt} + \Delta t \cdot \pmb{G}_{sh,frt})^{-1} \cdot \pmb{C}_{sh,frt} \cdot \pmb{\theta}_{r,n+1} \\
            & = \pmb{C}_{rm} \cdot \frac{1}{\Delta t} \cdot \pmb{\theta}_{r,n} \\
            & + \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot (\pmb{f}_{WSC,n+1} + \pmb{f}_{WSV,n+1}) \\
            & + c_a \cdot \rho_a \cdot \hat{\pmb{V}}_{vent,out,n} \cdot \pmb{\theta}_{o,n+1} \\
            & + \hat{\pmb{H}}_n \\
            & + \pmb{G}_{sh,frt} \cdot (\pmb{C}_{sh,frt} + \Delta t \cdot \pmb{G}_{sh,frt})^{-1}
            \cdot ( \pmb{C}_{sh,frt} \cdot \pmb{\theta}_{frt,n} + \Delta t \cdot \hat{\pmb{Q}}_{sol,frt,n+1} ) \\
            & + \hat{\pmb{L}}_{CS,n} \\
            & + \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot \pmb{f}_{WSB} \cdot \hat{\pmb{L}}_{RS,n} + \pmb{\beta} \cdot \hat{\pmb{L}}_{RS,n} \\
        \end{split}
        \tag{37}
    \end{align*}

となる。

ここで、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \pmb{f}_{BRM,n}
            & = \pmb{C}_{rm} \cdot \frac{1}{\Delta t}
            + \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot (\pmb{p}_{ji} - \pmb{f}_{WSR}) \\
            &+ c_a \cdot \rho_a \cdot ( \hat{\pmb{V}}_{vent,out,n} - \hat{\pmb{V}}_{vent,int,n} ) \\
            &+ \pmb{G}_{sh,frt} \cdot (\pmb{C}_{sh,frt} + \Delta t \cdot \pmb{G}_{sh,frt})^{-1} \cdot \pmb{C}_{sh,frt}
        \end{split}
        \tag{38}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \pmb{f}_{BRC,n}
            & = \pmb{C}_{rm} \cdot \frac{1}{\Delta t} \cdot \pmb{\theta}_{r,n}
            + \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot (\pmb{f}_{WSC,n+1} + \pmb{f}_{WSV,n+1}) \\
            & + c_a \cdot \rho_a \cdot \hat{\pmb{V}}_{vent,out,n} \cdot \pmb{\theta}_{o,n+1} + \hat{\pmb{H}}_n \\
            & + \pmb{G}_{sh,frt} \cdot (\pmb{C}_{sh,frt} + \Delta t \cdot \pmb{G}_{sh,frt})^{-1}
            \cdot ( \pmb{C}_{sh,frt} \cdot \pmb{\theta}_{frt,n} + \Delta t \cdot \hat{\pmb{Q}}_{sol,frt,n+1} )
        \end{split}
        \tag{39}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{BRL} = \pmb{p}_{ji}^{T} \cdot \pmb{h}_{s,c} \cdot \pmb{A}_{s} \cdot \pmb{f}_{WSB} + \pmb{\beta}
        \tag{40}
    \end{align*}

とすると、式(37)は、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{BRM,n} \cdot \pmb{\theta}_{r,n+1}
        = \pmb{f}_{BRC,n} + \hat{\pmb{L}}_{CS,n} + \pmb{f}_{BRL} \cdot \hat{\pmb{L}}_{RS,n}
        \tag{41}
    \end{align*}

のように表される。

------------------------------------------------------------------------------------------------------------------------
3. 作用温度と室温
------------------------------------------------------------------------------------------------------------------------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1) 作用温度
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

作用温度は次式で表される。

.. math::
    :nowrap:

    \begin{align*}
        \theta_{OT,i,n+1}
        = k_{c,i,n+1} \cdot \theta_{r,i,n+1} + k_{r,i,n+1} \cdot \theta_{MRT,hum,i,n+1}
        \tag{42}
    \end{align*}

ここで、

:math:`\theta_{OT,i,n+1}` : ステップ |n+1| における室 |i| の作用温度, ℃

:math:`\theta_{MRT,hum,i,n+1}` : ステップ |n+1| における室 |i| に居る人体に対する平均放射温度, ℃

:math:`k_{c,i,n+1}` : ステップ |n+1| における室 |i| の人体表面の対流熱伝達率が総合熱伝達率に占める割合

:math:`k_{r,i,n+1}` : ステップ |n+1| における室 |i| の人体表面の放射熱伝達率が総合熱伝達率に占める割合

である。

式(42)を室 :math:`0` ～ :math:`I-1` でベクトル表記をすると、式(43)となる。


.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{OT,n+1}
        = \pmb{k}_{c,n+1} \cdot \pmb{\theta}_{r,n+1} + \pmb{k}_{r,n+1} \cdot \pmb{\theta}_{MRT,hum,n+1}
        \tag{43}
    \end{align*}

ここで、

:math:`\pmb{\theta}_{OT,n+1}` : :math:`\theta_{OT,i,n+1}` を要素にもつ :math:`I \times 1` の縦行列, ℃

:math:`\pmb{\theta}_{MRT,hum,n+1}` : :math:`\theta_{MRT,hum,i,n+1}` を要素にもつ :math:`I \times 1` の縦行列, ℃

:math:`\pmb{k}_{c,n+1}` : :math:`k_{c,i,n+1}` を要素にもつ :math:`I \times I` の対角化行列

:math:`\pmb{k}_{r,n+1}` : :math:`k_{r,i,n+1}` を要素にもつ :math:`I \times I` の対角化行列

である。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2) 平均放射温度
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ステップ |n+1| における室 |i| に居る人体に対する平均放射温度は式(44)で表される。

.. math::
    :nowrap:

    \begin{align*}
        \theta_{MRT,hum,i,n+1} = \sum_j{f_{mrt,hum,i,j} \cdot \theta_{s,j,n+1}}
        \tag{44}
    \end{align*}

ここで、

:math:`f_{mrt,hum,i,j}` : 境界 |j| の表面温度が室 |i| に居る人体に与える放射の影響

である。

式(44)を室 :math:`0` ～ :math:`I-1` でベクトル表記をすると、式(45)となる。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{MRT,hum,n+1} = \pmb{f}_{mrt,hum} \cdot \pmb{\theta}_{s,n+1}
        \tag{45}
    \end{align*}

ここで、

:math:`\pmb{f}_{mrt,hum}` : :math:`f_{mrt,hum,i,j}` を要素にもつ :math:`I \times J` の行列

である。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3) 室温と作用温度との関係式の整理
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

式(43)に式(45)及び式(24)を代入する。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \pmb{\theta}_{OT,n+1}
            & = \pmb{k}_{c,n+1} \cdot \pmb{\theta}_{r,n+1} + \pmb{k}_{r,n+1} \cdot \pmb{\theta}_{MRT,hum,n+1} \\
            & = \pmb{k}_{c,n+1} \cdot \pmb{\theta}_{r,n+1} \\
            & + \pmb{k}_{r,n+1} \cdot \pmb{f}_{mrt,hum} \\
            & \cdot ( \pmb{f}_{WSR} \cdot \pmb{\theta}_{r,n+1} + \pmb{f}_{WSC,n+1} + \pmb{f}_{WSB} \cdot \pmb{L}_{RS,n+1} + \pmb{f}_{WSV,n+1} )
        \end{split}
        \tag{46}
    \end{align*}

この式を :math:`\pmb{\theta}_{r,n+1}` について解くと、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            &( \pmb{k}_{c,n+1} + \pmb{k}_{r,n+1} \cdot \pmb{f}_{mrt,hum} \cdot \pmb{f}_{WSR} ) \cdot \pmb{\theta}_{r,n+1} \\
            & = \pmb{\theta}_{OT,n+1} \\
            &- \pmb{k}_{r,n+1} \cdot \pmb{f}_{mrt,hum} \cdot \pmb{f}_{WSB} \cdot \hat{\pmb{L}}_{RS,n} \\
            &- \pmb{k}_{r,n+1} \cdot \pmb{f}_{mrt,hum} \cdot ( \pmb{f}_{WSC,n+1} + \pmb{f}_{WSV,n+1} )
        \end{split}
        \tag{47}
    \end{align*}

となる。

なお、式(37)における式変形と同様に、　:math:`\pmb{L}_{RS,n+1}` を :math:`\hat{\pmb{L}}_{RS,n}` で代表させている。


ここで、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{XOT,n+1} = ( \pmb{k}_{c,n+1} + \pmb{k}_{r,n+1} \cdot \pmb{f}_{mrt,hum} \cdot \pmb{f}_{WSR} ) ^ {-1}
        \tag{48}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{XLR,n+1} = - \pmb{f}_{XOT,n+1} \cdot \pmb{k}_{r,n+1} \cdot \pmb{f}_{mrt,hum} \cdot \pmb{f}_{WSB}
        \tag{49}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}_{XC,n+1}
        = - \pmb{f}_{XOT,n+1} \cdot \pmb{k}_{r,n+1} \cdot \pmb{f}_{mrt,hum} \cdot (\pmb{f}_{WSC,n+1} + \pmb{f}_{WSV,n+1})
        \tag{50}
    \end{align*}

とおくと、式(47)は、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{r,n+1}
        = \pmb{f}_{XOT,n+1} \cdot \pmb{\theta}_{OT,n+1} + \pmb{f}_{XLR,n+1} \cdot \hat{\pmb{L}}_{RS,n} + \pmb{f}_{XC,n+1}
        \tag{51}
    \end{align*}

となる。

------------------------------------------------------------------------------------------------------------------------
4. 作用温度と負荷
------------------------------------------------------------------------------------------------------------------------

式(41)に式(51)を代入すると次式となる。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            & \pmb{f}_{BRM,n} \cdot (
            \pmb{f}_{XOT,n+1} \cdot \pmb{\theta}_{OT,n+1} + \pmb{f}_{XLR,n+1} \cdot \hat{\pmb{L}}_{RS,n} + \pmb{f}_{XC,n+1}
            ) \\
            & = \pmb{f}_{BRC,n} + \hat{\pmb{L}}_{CS,n} + \pmb{f}_{BRL} \cdot \hat{\pmb{L}}_{RS,n}
        \end{split}
        \tag{52}
    \end{align*}

この式を整理すると、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            (\pmb{f}_{BRM,n} \cdot \pmb{f}_{XOT,n+1}) \cdot \pmb{\theta}_{OT,n+1}
            & = \hat{\pmb{L}}_{CS,n} \\
            & + ( \pmb{f}_{BRL} - \pmb{f}_{BRM,n} \cdot \pmb{f}_{XLR,n+1} ) \cdot \hat{\pmb{L}}_{RS,n} \\
            & + ( \pmb{f}_{BRC,n} - \pmb{f}_{BRM,n} \cdot \pmb{f}_{XC,n+1} )
        \end{split}
        \tag{53}
    \end{align*}

となる。この式は、作用温度 :math:`\pmb{\theta}_{OT,n+1}` と
対流空調の放熱量 :math:`\hat{\pmb{L}}_{RS,n}` 及び放射空調の放熱量 :math:`\hat{\pmb{L}}_{RS,n}` のバランス式となっているため、
3つの変数のうち、どれか1つを未知数と置くことで、負荷または作用温度を計算することができる。

なお、室温を指定して負荷計算を行う場合は、

.. math::
    :nowrap:

    \begin{align*}
        k_{c,i,n+1} = 1.0
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        k_{r,i,n+1} = 0.0
    \end{align*}

とおけば良い。

------------------------------------------------------------------------------------------------------------------------
5. 地盤の計算
------------------------------------------------------------------------------------------------------------------------

地盤の熱容量は大きいため、建物全体の計算よりも助走時間を長く（例えば最低でも1年など）とらなければならない。
このような長い時間の助走計算を建物全体で行うと計算時間が非常にかかってしまうため、最初に地盤のみである程度長い時間の助走計算を行い、その後、短い時間で建物全体の助走計算を行うことにする。
地盤のみで助走計算を行う場合、室内側の空気温度は建物全体の熱バランスを解いていないため分からない。
そこで、地盤のみの助走計算を行うにあたって室内側の空気温度を外気温度に仮定して解くことにする。

境界表面温度の式(4)、式(5)及び式(6)を再掲する。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{s,n+1} = \pmb{\phi}_{a0} \cdot \pmb{q}_{s,n+1} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}}
        + \pmb{\phi}_{t0} \cdot \pmb{\theta}_{s,rear,n+1} + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        \tag{4}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}'_{s,a,m,n+1} = \pmb{\phi}_{a1,m} \cdot \pmb{q}_{s,n} + \pmb{r}_{m} \cdot \pmb{\theta}'_{s,a,m,n}
        \tag{5}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}'_{s,t,m,n+1}
        = \pmb{\phi}_{t1,m} \cdot \pmb{\theta}_{s,rear,n} + \pmb{r}_{m} \cdot \pmb{\theta}'_{s,t,m,n}
        \tag{6}
    \end{align*}

表面熱流の式(8)を再掲する。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{q}_{s,n} = \pmb{h}_{s,i} \cdot ( \pmb{\theta}_{er,n} - \pmb{\theta}_{s,n} )
        \tag{8}
    \end{align*}

ここで、式(8)の表面熱流の式を1ステップ進めると、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{q}_{s,n+1} = \pmb{h}_{s,i} \cdot ( \pmb{\theta}_{er,n+1} - \pmb{\theta}_{s,n+1} )
        \tag{54}
    \end{align*}

となる。この式を式(4)に代入すると、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{s,n+1} = \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i} \cdot ( \pmb{\theta}_{er,n+1} - \pmb{\theta}_{s,n+1} )
        + \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}}
        + \pmb{\phi}_{t0} \cdot \pmb{\theta}_{s,rear,n+1}
        + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        \tag{55}
    \end{align*}

となり、 :math:`\pmb{\theta}_{s,n+1}` について解くと、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{s,n+1} = (\pmb{I} + \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i}) ^ {-1} \cdot
        ( \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i} \cdot \pmb{\theta}_{er,n+1}
        + \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}}
        + \pmb{\phi}_{t0} \cdot \pmb{\theta}_{s,rear,n+1}
        + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        )
        \tag{56}
    \end{align*}


となる。ここで、室内側の等価室温である :math:`\pmb{\theta}_{er,n+1}` は外気温度で代用するため、 :math:`\pmb{\theta}_{o,n+1}` と書き換えると、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\theta}_{s,n+1} = (\pmb{I} + \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i}) ^ {-1} \cdot
        ( \pmb{\phi}_{a0} \cdot \pmb{h}_{s,i} \cdot \pmb{\theta}_{o,n+1}
        + \sum_{m=1}^{M}{\pmb{\theta}'_{s,a,m,n+1}}
        + \pmb{\phi}_{t0} \cdot \pmb{\theta}_{s,rear,n+1}
        + \sum_{m=1}^{M}{\pmb{\theta}'_{s,t,m,n+1}}
        )
        \tag{57}
    \end{align*}

であり、式(54)は

.. math::
    :nowrap:

    \begin{align*}
        \pmb{q}_{s,n+1} = \pmb{h}_{s,i} \cdot ( \pmb{\theta}_{o,n+1} - \pmb{\theta}_{s,n+1} )
        \tag{58}
    \end{align*}

となる。


------------------------------------------------------------------------------------------------------------------------
6. 具体的な解法の手順
------------------------------------------------------------------------------------------------------------------------

これまで定式化した数式における記号は以下の3種類に分類される。

イ） 時刻によって変動しない値（形態係数など）

ロ） 時刻によって変動するが他の時刻の影響を受けない値（日射量など）

ハ） 時刻によって変動し、かつ、前の時刻の状態に影響を受ける値（室温など）

今回の計算のほとんどの部分は、ハ）の値を算出するために最初のステップ（ :math:`n = 0` ）から逐次ステップ数をインクリメントして計算していく部分である。

今後の説明において、イ）とロ）は既知のものとして扱い、特に断りの無い限り、その計算方法は別の箇所で記述する。
ステップ |n+1| の状態を計算するのに必要なステップ |n| の状態を表す最低限のパラメータは以下のとおりである。
なお、ここで引き渡す値については特にこれでないといけないという決まりはない。
（例えば :math:`\pmb{q}_{s,n}` の代わりに :math:`\pmb{\theta}_{s,ei,n+1}` を引き渡しても良い。）
計算の前後関係から、なるべく引き渡すパラメータの数が少なくなるように配慮して選定した。

また、以下に示すパラメータについては、暖冷房の運転状態やPMV等の何らかのステップ |n| における状態から決定される値とした。
なお、ここで挙げるパラメータの決め方については、記述を省略する。

:math:`\hat{\pmb{V}}_{vent,out,n}`

:math:`\hat{\pmb{V}_{vent,int,n}}`

:math:`\pmb{k}_{r,n+1}`

:math:`\pmb{k}_{c,n+1}`

関係図を以下に示す。
各パラメータの関係は非常に複雑なため、作用温度を求めるまでの計算と作用温度を求めてからの各種温度計算（ポスト処理）とに分けて記述する。

変数種類イ）については以下のフローにより計算する。

.. image:: ../_static/images/heat_load_balance_1.png
    :scale: 50%

図1 変数種類イ）の計算フロー

負荷または自然室温を計算するフローを以下に示す。

.. image:: ../_static/images/heat_load_balance_2.png
    :scale: 50%

図2 負荷または自然室温の計算フロー

負荷および自然室温を計算した後のフローを以下に示す。

.. image:: ../_static/images/heat_load_balance_3.png
    :scale: 50%

図3 負荷および自然室温計算後の計算フロー


