.. |i| replace:: :math:`i`
.. |j| replace:: :math:`j`
.. |k| replace:: :math:`k`
.. |m3| replace:: m\ :sup:`3` \
.. |n| replace:: :math:`n`
.. |n+1| replace:: :math:`n+1`

************************************************************************************************************************
繰り返し計算（湿度と潜熱）
************************************************************************************************************************

========================================================================================================================
I. 評価法
========================================================================================================================

------------------------------------------------------------------------------------------------------------------------
1. 次のステップの絶対湿度と潜熱負荷（絶対湿度を設定する場合（住宅・非住宅用））
------------------------------------------------------------------------------------------------------------------------

ステップ |n| からステップ |n+1| における室 |i| の
潜熱負荷（加湿を正・除湿を負とする） :math:`\hat{L}_{L,i,n}` は、式(1)により計算される。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\hat{L}}_{L,n} = \pmb{\hat{L}}''_{a,n} \cdot \pmb{X}_{r,n+1} + \pmb{\hat{L}}''_{b,n} \tag{1}
    \end{align*}

ここで、

:math:`\pmb{\hat{L}}_{L,n}`
    | :math:`\hat{L}_{L,i,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / s
:math:`\pmb{\hat{L}}''_{a,n}`
    | :math:`\hat{L}''_{a,i,j,n}` を要素にもつ :math:`N_{room} \times N_{room}` の正方行列, kg / s(kg/kg(DA))
:math:`\pmb{X}_{r,n+1}`
    | :math:`X_{r,i,n+1}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / kg(DA)
:math:`\pmb{\hat{L}}''_{b,n}`
    | :math:`\hat{L}''_{b,i,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / s

であり、

:math:`\hat{L}_{L,i,n}`
    | ステップ |n| から |n+1| における室 |i| の潜熱負荷（加湿を正・除湿を負とする）, kg / s
:math:`\hat{L}''_{a,i,j,n}`
    | ステップ |n+1| における室 |j| の絶対湿度がステップ |n| から |n+1| における室 |i| の潜熱負荷に与える影響を表す係数, kg / s(kg/kg(DA))
:math:`X_{r,i,n+1}`
    | ステップ |n+1| における室 |i| の絶対湿度, kg / kg(DA)
:math:`\hat{L}''_{b,i,n}`
    | ステップ |n| から |n+1| における室 |i| の潜熱負荷に与える影響を表す係数, kg / s

である。ここで、 :math:`N_{room}` は室の数を表す。

ステップ |n+1| における室 |i| の絶対湿度 :math:`X_{r,i,n+1}` は式(2a)で、
ステップ |n| から |n+1| における係数 :math:`\hat{L}''_{a,i,n}`　は式(2b)で、
ステップ |n| から |n+1| における係数 :math:`\hat{L}''_{b,i,n}`　は式(2c)で表される。

.. math::
    :nowrap:

    \begin{align*}
        X_{r,i,n+1} = \begin{cases}
            k_{i,n} & ( \hat{f}_{set,i,n} = 0, \text{絶対湿度を設定しない場合} ) \\
            X'_{r,set,i,n+1} & ( \hat{f}_{set,i,n} = 1, \text{絶対湿度を設定する場合} )
        \end{cases}
        \tag {2a}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}''_{a,i,j,n} = \hat{L}'_{a,i,j,n} \tag{2b}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}''_{b,i,n} = \begin{cases}
            \hat{L}'_{b,i,n} & ( \hat{f}_{set,i,n} = 0, \text{絶対湿度を設定しない場合} ) \\
		    k_{i,n} & ( \hat{f}_{set,i,n} = 1, \text{絶対湿度を設定する場合} )
        \end{cases}
        \tag{2c}
    \end{align*}

ここで、

:math:`X'_{r,set,i,n+1}`
    | ステップ |n+1| における室 |i| の設定絶対湿度（設定しない場合は0とする）, kg / kg(DA)
:math:`\hat{L}'_{a,i,j,n}`
    | ステップ |n+1| における室 |j| の絶対湿度がステップ |n| から |n+1| における室 |i| の潜熱負荷に与える影響を表す係数, kg / s(kg/kg(DA))
:math:`\hat{L}'_{b,i,n}`
    | ステップ |n| から |n+1| における室 |i| の潜熱負荷に与える影響を表す係数, kg / s
:math:`\hat{f}_{set,i,n}`
    | ステップ |n| から |n+1| における室 |i| の絶対湿度を設定するか否かを表す記号（設定する場合を1とし、設定しない場合を0とする。）

であり、
:math:`k_{i,n}` は、 :math:`\hat{f}_{set,i,n} = 0` の時（絶対湿度を設定しない時）は、
成り行きで求まるステップ |n+1| における室 |i| の絶対湿度を表し、
:math:`\hat{f}_{set,i,n+1} = 1` の時（絶対湿度を設定する時）は、
それに必要なステップ |n| から |n+1| における室 |i| の潜熱負荷を表す。
絶対湿度を設定するか否かに応じて単位が異なることに留意されたい。

係数 :math:`k_{i,n}` は式(3)で表される。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{k}_n　= {\pmb{F}''}_{h,wgt,n}^{-1} \cdot ( - \pmb{F}'_{h,wgt,n} \cdot \pmb{X}'_{r,set,n+1} + \pmb{F}_{h,cst,n} + \pmb{\hat{L}}'_{b,n} )　\tag{3}
    \end{align*}

ここで、

:math:`\pmb{k}_n`
    | :math:`k_{i,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg/kg(DA) または kg / s
:math:`{\pmb{F}''}_{h,wgt,n}`
    | :math:`{F''}_{h,wgt,i,j,n}` を要素にもつ :math:`N_{room} \times N_{room}` の正方行列, kg / s(kg/kg(DA)) または -
:math:`{\pmb{F}'}_{h,wgt,n}`
    | :math:`{F'}_{h,wgt,i,j,n}` を要素にもつ :math:`N_{room} \times N_{room}` の正方行列, kg / s(kg/kg(DA)) または -
:math:`\pmb{X}'_{r,set,n+1}`
    | :math:`X'_{r,set,i,n+1}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / kg(DA)
:math:`\pmb{F}_{h,cst,n}`
    | :math:`F_{h,cst,i,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / s
:math:`\pmb{\hat{L}}'_{b,n}`
    | :math:`\hat{L}'_{b,i,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / s

である。

係数 :math:`F''_{h,wgt,i,j,n}` は式(4)で表される。

.. math::
    :nowrap:

    \begin{align*}
    	F''_{h,wgt,i,j,n} = \begin{cases}
            F'_{h,wgt,i,j,n} & ( \hat{f}_{set,j,n} = 0 ) \\
            - \delta_{ij} & ( \hat{f}_{set,j,n} = 1 )
        \end{cases}
    	\tag{4}
    \end{align*}

ここで、 :math:`\delta_{ij}` はクロネッカーのデルタである。

係数 :math:`F'_{h,wgt,i,j,n}` は式(5)で表される。

.. math::
    :nowrap:

    \begin{align*}
        F'_{h,wgt,i,j,n} = F_{h,wgt,i,j,n} - \hat{L}'_{a,i,j,n} \tag{5}
    \end{align*}

:math:`X'_{r,set,i,n+1}` はステップ |n+1| における室 |i| の設定絶対湿度（設定しない場合は0とする)を表すため、
絶対湿度を設定する場合は、後述するステップ |n+1| における室 |i| の設定絶対湿度 :math:`X_{r,set,i,n+1} とし、
絶対湿度を設定しない場合は0とする。

:math:`\hat{L}'_{a,i,j,n}` は、
室 |I| において絶対湿度を設定する場合は、

.. math::
    :nowrap:

    \begin{align*}
        {{\hat{L}'_{a,i,j,n}} \vert}_{i=I} = 0
    \end{align*}

絶対湿度を設定しない場合は、

.. math::
    :nowrap:

    \begin{align*}
        {{\hat{L}'_{a,i,j,n}} \vert}_{i \neq I} = \hat{L}_{a,i,j,n}
    \end{align*}

であり、
:math:`\hat{L}'_{b,i,n}` は、
室 |I| において絶対湿度を設定する場合は、

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}'_{b,i,n} = 0
    \end{align*}

絶対湿度を設定しない場合は、

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}'_{b,i,n} = \hat{L}_{b,i,n}
    \end{align*}

である。

ここで、

:math:`\hat{L}_{a,i,j,n}`
    | ステップ |n+1| における室 |j| の絶対湿度がステップ |n| から |n+1| における室 |i| の潜熱負荷に与える影響を表す係数, kg / s(kg/kg(DA))
:math:`\hat{L}_{b,i,n}`
    | ステップ |n| から |n+1| における室 |i| の潜熱負荷に与える影響を表す係数, kg / s

であり、後述する、ステップ |n+1| における室 |i| の加湿・除湿を行わない場合の絶対湿度 :math:`X_{r,ntr,i,n+1}` に応じて定まり、
その決定方法は、付録Aに示す。

------------------------------------------------------------------------------------------------------------------------
2. 次のステップの絶対湿度と潜熱負荷（絶対湿度を設定しない場合（住宅用））
------------------------------------------------------------------------------------------------------------------------

ステップ |n| からステップ |n+1| における室 |i| の
潜熱負荷（加湿を正・除湿を負とする） :math:`\hat{L}_{L,i,n}` は、式(6)により計算される。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\hat{L}}_{L,n} = \pmb{\hat{L}}_{a,n} \cdot \pmb{X}_{r,n+1} + \pmb{\hat{L}}_{b,n} \tag{6}
    \end{align*}

ここで、

:math:`\pmb{\hat{L}}_{L,n}`
    | :math:`\hat{L}_{L,i,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / s
:math:`\pmb{\hat{L}}_{a,n}`
    | :math:`\hat{L}_{a,i,j,n}` を要素にもつ :math:`N_{room} \times N_{room}` の正方行列, kg / s(kg/kg(DA))
:math:`\pmb{X}_{r,n+1}`
    | :math:`X_{r,i,n+1}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / kg(DA)
:math:`\pmb{\hat{L}}_{b,n}`
    | :math:`\hat{L}_{b,i,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / s

であり、

:math:`\hat{L}_{L,i,n}`
    | ステップ |n| から |n+1| における室 |i| の潜熱負荷（加湿を正・除湿を負とする）, kg / s
:math:`\hat{L}_{a,i,j,n}`
    | ステップ |n+1| における室 |j| の絶対湿度がステップ |n| から |n+1| における室 |i| の潜熱負荷に与える影響を表す係数, kg / s(kg/kg(DA))
:math:`X_{r,i,n+1}`
    | ステップ |n+1| における室 |i| の絶対湿度, kg / kg(DA)
:math:`\hat{L}_{b,i,n}`
    | ステップ |n| から |n+1| における室 |i| の潜熱負荷に与える影響を表す係数, kg / s

である。ここで、 :math:`N_{room}` は室の数を表す。


ステップ |n+1| における絶対湿度 :math:`\pmb{X}_{r,n+1}` は式(7)で表される。

.. math::
    :nowrap:

    \begin{align*}
        \pmb{X}_{r,n+1}　= {\pmb{F}'}_{h,wgt,n}^{-1} \cdot ( \pmb{F}_{h,cst,n} + \pmb{\hat{L}}_{b,n} )　\tag{7}
    \end{align*}

ここで、

:math:`{\pmb{F}'}_{h,wgt,n}`
    | :math:`{F'}_{h,wgt,i,j,n}` を要素にもつ :math:`N_{room} \times N_{room}` の正方行列, kg / s(kg/kg(DA)) または -
:math:`\pmb{F}_{h,cst,n}`
    | :math:`F_{h,cst,i,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / s
:math:`\pmb{\hat{L}}_{b,n}`
    | :math:`\hat{L}_{b,n}` を要素にもつ :math:`N_{room} \times 1` の縦行列, kg / s

である。

係数 :math:`F'_{h,wgt,i,j,n}` は式(8)で表される。

.. math::
    :nowrap:

    \begin{align*}
        F'_{h,wgt,i,j,n} = F_{h,wgt,i,j,n} - \hat{L}_{a,i,j,n} \tag{8}
    \end{align*}

:math:`\hat{L}_{a,i,j,n}` 及び :math:`\pmb{\hat{L}}_{b,n}` は、
後述する、ステップ |n+1| における室 |i| の加湿・除湿を行わない場合の絶対湿度 :math:`X_{r,ntr,i,n+1}` に応じて定まり、
その決定方法は、付録Aに示す。

------------------------------------------------------------------------------------------------------------------------
3. 加湿・除湿を行わない場合の次のステップの絶対湿度
------------------------------------------------------------------------------------------------------------------------

加湿・除湿を行わない場合のステップ |n+1| における室 |i| の絶対湿度 :math:`X_{r,ntr,i,n+1}` は式(9)で表される。

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{X}_{r,ntr,n+1}　= \pmb{F}_{h,wgt,n}^{-1} \cdot \pmb{F}_{h,cst,n}　\tag{9}
    \end{align*}

ここで、

:math:`\pmb{X}_{r,ntr,n+1}`
    | :math:`X_{r,ntr,i,n+1}` を要素にもつ :math:`I \times 1` の縦行列, kg / kg(DA)

であり、

:math:`X_{r,ntr,i,n+1}`
    | ステップ |n+1| における室 |i| の加湿・除湿を行わない場合の絶対湿度, kg / kg(DA)

である。

------------------------------------------------------------------------------------------------------------------------
4. 係数 :math:`F_{h,wgt}` ・係数 :math:`F_{h,cst}`
------------------------------------------------------------------------------------------------------------------------

ステップ |n| における係数 :math:`F_{h,wgt,i,j,n}` は式(10)で表される。

.. math::
    :nowrap:

    \begin{align*}
    	F_{h,wgt,i,j,n}
	    &= \left( \rho_a \cdot \left( \frac{ V_{room,i} }{ \Delta t } + \hat{V}_{out,vent,i,n} \right) + \frac{ G_{lh,frt,i} \cdot C_{lh,frt,i} }{ C_{lh,frt,i} + \Delta t \cdot G_{lh,frt,i} } \right) \cdot \delta_{ij} \\
    	&- \rho_a \cdot \left( \hat{V}_{int,vent,i,j,n} - \delta_{ij} \cdot \sum_{k=0}^{N_{room}-1}{\hat{V}_{int,vent,i,k,n}} \right)
    	\tag{10}
    \end{align*}

ここで、

:math:`\rho_a`
    | 空気の密度, kg / |m3| 
:math:`V_{room,i}`
    | 室 |i| の容積, |m3| 
:math:`\Delta t`
    | 1ステップの時間間隔, s 
:math:`\hat{V}_{out,vent,i,n}`
    | ステップ |n| から |n+1| における室 |i| の外気との換気量, |m3| / s
:math:`G_{lh,frt,i}`
    | 室 |i| の備品等と空気間の湿気コンダクタンス, kg / (s kg/kg(DA))
:math:`C_{lh,frt,i}`
    | 室 |i| の備品等の湿気容量, kg / (kg/kg(DA))
:math:`\hat{V}_{int,vent,i,j,n}`
    | 室 |j| から室 |i| への室間の機械換気量, |m3| / s
:math:`\hat{V}_{int,vent,i,k,n}`
    | 室 |k| から室 |i| への室間の機械換気量, |m3| / s

である。

ステップ |n| における室の湿度に関する係数 :math:`F_{h,cst,i,n}` は式(11)で表される。

.. math::
    :nowrap:

    \begin{align*}
    	F_{h,cst,i,n}
        &= \rho_a \cdot \frac{ V_{room,i} }{ \Delta t } \cdot X_{r,i,n}
    	+ \rho_a \cdot \hat{V}_{out,vent,i,n} \cdot X_{o,n+1} \\
	    &+ \frac{G_{lh,frt,i} \cdot C_{lh,frt,i} }{ C_{lh,frt,i} + \Delta t \cdot G_{lh,frt,i} } \cdot X_{frt,i,n}
    	+ \hat{X}_{gen,i,n} + \hat{X}_{hum,i,n}
        \tag{11}
    \end{align*}

ここで、

:math:`X_{o,n}`
    | ステップ |n| における外気絶対湿度, kg/kg(DA)
:math:`X_{frt,i,n}`
    | ステップ |n| における室 |i| の備品等の絶対湿度, kg/kg(DA)
:math:`\hat{X}_{gen,i,n}`
    | ステップ |n| における室 |i| の人体発湿を除く内部発湿, kg/s
:math:`\hat{X}_{hum,i,n}`
    | ステップ |n| における室 |i| の人体発湿, kg/s

である。

------------------------------------------------------------------------------------------------------------------------
付録A 係数 :math:`\hat{L}_a` ・係数 :math:`\hat{L}_b`
------------------------------------------------------------------------------------------------------------------------

係数 :math:`\hat{L}_{a,n}` 及び :math:`\hat{L}_{b,n}` の定め方について、設備の種類ごとに記述する。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A.1. 除湿・加湿を行わない場合
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ステップ |n| から |n+1| における室 |i| において除湿・加湿を行わない場合は以下のように定める。

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}_{a,i,j,n} = 0 \tag{A.1a}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}_{b,i,n} = 0 \tag{A.1b}
    \end{align*}

ここで、 :math:`j = 0 \ldots N_{room} - 1` である。


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A.2. 一定量の除湿・加湿を行う場合
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ステップ |n| から |n+1| における室 |i| において一定量の除湿・加湿を行う場合は以下のように定める。

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}_{a,i,j,n} = 0 \tag{A.2a}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}_{b,i,n} = \hat{q}_{X,i,n} \tag{A.2b}
    \end{align*}

ここで、

:math:`\hat{q}_{X,i,n}`
    | ステップ |n| から |n+1| における室 |i| の加湿・除湿量（加湿を正・除湿を負とする）, kg / s

である。
また、 :math:`j = 0 \ldots N_{room} - 1` である。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A.3.　絶対湿度に応じて一定量の除湿を行う場合（ルームエアコンディショナー）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ルームエアコンディショナーを設置する室の集合を :math:`\pmb{k}` とする。
ステップ |n| から |n+1| における室 |i| において、
ステップ |n+1| における室 |i| の絶対湿度に応じて一定量の除湿を行う場合は以下のように定める。

.. math::
    :nowrap:

    \begin{align*}
        \left. \hat{L}_{a,i,j,n} \right|_{i \in \pmb{k}} = \begin{cases}
            - \hat{V}_{rac,i,n} \cdot \rho_a \cdot ( 1 - BF_{rac,i} ) \cdot \delta_{ij} & \begin{pmatrix} X_{r,ntr,i,n+1} > X_{rac,ex-srf,i,n+1} \\ \text{and} \\ \hat{q}_{s,i,n} > 0 \end{pmatrix} \\
            0 & \left( \text{その他の場合} \right)
        \end{cases}
        \tag{A.3a}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
        \left. \hat{L}_{b,i,n} \right|_{i \in \pmb{k}} = \begin{cases}
            \hat{V}_{rac,i,n} \cdot \rho_a \cdot ( 1 - BF_{rac,i} ) \cdot X_{rac,ex-srf,i,n+1} & \begin{pmatrix} X_{r,ntr,i,n+1} > X_{rac,ex-srf,i,n+1} \\ \text{and} \\ \hat{q}_{s,i,n} > 0 \end{pmatrix} \\
            0 & \left( \text{その他の場合} \right)
        \end{cases}
        \tag{A.3b}
    \end{align*}

ここで、

:math:`\hat{V}_{rac,i,n}`
    | ステップ |n| から |n+1| における室 |i| に設置されたルームエアコンディショナーの吹き出し風量, |m3| / s
:math:`\rho_a`
    空気の密度, kg / |m3| 
:math:`BF_{rac,i}`
    室 |i| に設置されたルームエアコンディショナーの室内機の熱交換器のバイパスファクター, -
:math:`X_{rac,ex-srf,i,n+1}`
    ステップ |n+1| における室 |i| に設置されたルームエアコンディショナーの室内機の熱交換器表面絶対湿度, kg/kg(DA)

である。

ステップ |n+1| における室 |i| に設置されたルームエアコンディショナーの室内機の熱交換器表面絶対湿度 :math:`X_{rac,ex-srf,i,n+1}` は式(A.4)で表される。

.. math::
    :nowrap:

    \begin{align*}
        X_{rac,ex-srf,i,n+1} = f_x \left( f_{p,vs} \left( \theta_{rac,ex-srf,i,n+1} \right) \right) \tag{A.4}
    \end{align*}

:math:`\theta_{rac,ex-srf,i,n+1}`
    | ステップ :math:`n+1` における室 :math:`i` に設置されたルームエアコンディショナーの室内機の熱交換器表面温度, ℃

また、関数 :math:`f_x` は、飽和水蒸気圧を飽和絶対湿度に変換する関数、関数 :math:`f_{p,vs}` は温度を飽和水蒸気圧に変換する関数である。

ステップ |n+1| における室 |i| に設置されたルームエアコンディショナーの室内機の熱交換器表面温度　:math:`\theta_{rac,ex-srf,i,n+1}` は式(A.5)で表される。

.. math::
    :nowrap:

    \begin{align*}
        \theta_{rac,ex-srf,i,n+1} = \theta_{r,i,n+1} - \frac{ \hat{q}_{s,i,n} }{ c_a \cdot \rho_a \cdot \hat{V}_{rac,i,n} \cdot (1 - BF_{rac,i}) } \tag{A.5}
    \end{align*}

ここで、

:math:`\theta_{r,i,n+1}`
    | ステップ |n+1| における室 |i| の温度, ℃
:math:`\hat{q}_{s,i,n}`
    | ステップ |n| から |n+1| における室 |i| の顕熱負荷, W
:math:`c_a`
    | 空気の比熱, J / kg K

である。

室 |i| に設置されたルームエアコンディショナーの室内機の熱交換器のバイパスファクター :math:`BF_{rac,i}` は 0.2 とする。

ステップ |n| から |n+1| における室 |i| に設置されたルームエアコンディショナーの吹き出し風量 :math:`\hat{V}_{rac,i,n}` は式(A.6)により表される。
ただし、計算された :math:`\hat{V}_{rac,i,n}` が :math:`V_{rac,min,i}` を下回る場合は :math:`V_{rac,min,i}` に等しいとし、
:math:`V_{rac,max,i}` を上回る場合は :math:`V_{rac,max,i}` に等しいとする。

.. math::
    :nowrap:

    \begin{align*}
        \hat{V}_{rac,i,n}
        = V_{rac,min,i} \cdot \frac{ q_{rac,max,i} - q_{s,i,n} }{ q_{rac,max,i} - q_{rac,min,i} }
        + V_{rac,max,i} \cdot \frac{ q_{rac,min,i} - q_{s,i,n} }{ q_{rac,min,i} - q_{rac,max,i} }
        \tag{A.6}
    \end{align*}

ここで、

:math:`V_{rac,min,i}`
    | 室 |i| に設置されたルームエアコンディショナーの最小能力時における風量, |m3| / s
:math:`V_{rac,max,i}`
    | 室 |i| に設置されたルームエアコンディショナーの最大能力時における風量, |m3| / s
:math:`q_{rac,min,i}`
    | 室 |i| に設置されたルームエアコンディショナーの最小能力, W
:math:`q_{rac,max,i}`
    | 室 |i| に設置されたルームエアコンディショナーの最大能力, W

である。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A.3.　絶対湿度に応じて一定量の除湿を行う場合（ダクト式セントラル空調）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. math::
    :nowrap:

    \begin{align*}
        \hat{L}_{a,i,j,n} = - \hat{V}_{RAC,i,n} \cdot \rho_a \cdot ( 1 - BF_{RAC,i} ) \tag{A.7a}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
    	\hat{L}_{b,i,n} = \hat{V}_{RAC,i,n} \cdot \rho_a \cdot ( 1 - BF_{RAC,i} ) \cdot X_{RAC,ex-srf,i} \tag{A.7b}
    \end{align*}

ここで、

:math:`\hat{V}_{RAC,i,n}`
    | ステップ |n| から |n+1| における室 |i| に設置されたルームエアコンディショナーの吹き出し風量, |m3| / s
:math:`\rho_a`
    | 空気の密度, kg / |m3| 
:math:`BF_{RAC,i}`
    | 室 |i| に設置されたルームエアコンディショナーの室内機の熱交換器のバイパスファクター, -
:math:`X_{RAC,ex-srf,i}`
    室 |i| に設置されたルームエアコンディショナーの室内機の熱交換器表面の絶対湿度, kg/kg(DA)

である。


========================================================================================================================
II. 根拠
========================================================================================================================

