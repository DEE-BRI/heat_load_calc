.. include:: definition.txt

.. raw:: latex

    \clearpage


========================================================================================================================
入力用 json ファイル
========================================================================================================================

建物の仕様やスケジュール等の使用方法を記述したプログラム入力用ファイルの仕様を記します。

------------------------------------------------------------------------------------------------------------------------
ルート
------------------------------------------------------------------------------------------------------------------------

ルート部分は次の要素で構成されています。

common (必須項目)
    | 空調方式などを記した common 要素です。
building (必須項目)
    | 建物全体に関する仕様を記した building 要素です。
rooms (必須項目)
    | 室の仕様を記した room 要素を配列で室の数だけ指定します。
boundaries (必須項目)
    | 外皮や室間の間仕切り等の境界の仕様を記した boundary 要素を配列で境界の数だけ指定します。
mechanical_ventilations (必須項目)
    | 換気経路の情報を記した mechanical_ventilation 要素を配列で換気経路の数だけ指定します。
    | なお、この機械換気には、通風利用による自然換気やレンジフード等の局所換気は含みません。
equipments (必須項目)
    | 設備の仕様を記した equipments 要素です。
    | equpments 要素はさらに暖房設備を記した heating_equipments 要素と、冷房設備を記した cooling_equipments 要素に分けられます。

.. code-block::
    :caption: root の記述例

    {
        "common": {...},
        "building": {...},
        "rooms": [
            {...},
            {...},
            ...
        ],
        "boundaries": [
            {...},
            {...},
            ...
        ],
        "mechanical_ventilations": [
            {...},
            {...},
            ...
        ],
        "equipments": {...}
    }

------------------------------------------------------------------------------------------------------------------------
common 要素
------------------------------------------------------------------------------------------------------------------------

common 要素は、唯一、以下の ac_method を持ちます。

ac_method (必須項目)
    | 空調の運転方式を表します。
    | 空調の運転方式として、指定されたPMVになるように空調する方法（PMV制御）と指定された作用温度になるように空調する方法（作用温度制御）の2種類が用意されています。
    | 空調の運転方式は文字列で指定します。
    | PMV 制御を指定する場合は、"pmv" とします。
    | 作用温度制御を指定する場合は、"simple" とします。

.. code-block::
    :caption: common 要素の記述例

    {
        "common": {
            "ac_method": "pmv"
        },
        ...
    }

------------------------------------------------------------------------------------------------------------------------
building 要素
------------------------------------------------------------------------------------------------------------------------

building 要素は、唯一、以下の infiltration 要素を持ちます。

infiltration (必須項目)
    | 漏気に関する設定を保持する infiltration 要素です。

.. code-block::
    :caption: building 要素の記述例

    {
        ...
        "building": {
            "infiltration": {...}
        },
        ...
    }

------------------------------------------------------------------------------------------------------------------------
infiltration 要素
------------------------------------------------------------------------------------------------------------------------

infiltration 要素は次の要素を持ちます。

method (必須項目)
    | 漏気量を計算する方法を選択します。
    | 建物の仕様から漏気量を計算する方法を指定します。
    | 現在、建物の仕様から漏気量を計算する方法は、 balance_residential メソッドのみです。
    | 文字列で、"balance_residential" と記します。
story (必須項目)
    | 建物の階数を表します。
    | 1 又は 2 を数値（整数型）で指定します。3 階以上の建物には対応していませんので、その場合は 2 と入力してください。
c_value_estimate (必須項目)
    | C値の指定方法を表します。specify と calculate が用意されています。
    | specify とは、C値を直接指定する方法です。
    | calculate とは、建物の構造とUA値からC値を推定する方法です。
c_value
    | 相当隙間面積を数値（小数点型）で表します。c_value_estimate 要素に specify が指定された場合のみ指定します。単位は |cm2| / |m2| です。0 以上の数字を入力します。
ua_value
    | UA値を数値（小数点型）で表します。c_value_estimate 要素に calculate が指定された場合のみ指定します。単位は W / ( |m2| K ) です。0 以上の数字を入力します。
struct
    | 建物の構造を表します。c_value_estimate 要素に calculate が指定された場合のみ指定します。
    | 文字列で、RC, SRC, WOODEN, STEEL から指定します。
    | RC は、鉄筋コンクリート造等を表します。
    | SRC は、鉄骨鉄筋コンクリート造を表します。
    | WOODEN は、木造を表します。
    | STEEL は、鉄骨造を表います。
    | これらの構造は、UA値とC値を紐づけるために指定する必要があります。
    | 鉄筋コンクリート造等と鉄骨鉄筋コンクリート造は結果は同じとなります。
    | 木造と鉄骨造は結果は同じとなります。
inside_pressure (必須項目)
    | 室内外の圧力差を入力します。positive, negative, balanced から選択します。
    | positive とは室内圧力が室外圧力よりも高い状態を表します。換気方式として第2種換気を採用した場合には、positive を指定するのがよいでしょう。
    | negative とは室内圧力が室外圧力よりも低い状態を表します。換気方式として第3種換気を採用した場合には、negative を指定するのがよいでしょう。
    | balanced とは室内圧力と室外圧力が釣り合っている状態を表します。換気方式として第1種換気を採用した場合には、alanced を指定するのがよいでしょう。

.. code-block::
    :caption: infiltration 要素の記述例（C値を指定する場合）

    {
        ...
        "building": {
            "infiltration": {
                "method": "balance_residential",
                "story": 2,
                "c_value_estimate": "specify",
                "c_value": 2.3,
                "inside_pressure": "negative"
            }
        },
        ...
    }

.. code-block::
    :caption: infiltration 要素の記述例（C値をUA値や建物の構造から推定する場合）

    {
        ...
        "building": {
            "infiltration": {
                "method": "balance_residential",
                "story": "2",                
                "c_value_estimate": "calculate",
                "ua_value": 2.5,
                "struct": "RC",
                "inside_pressure": "negative"
            }
        },
        ...
    }

------------------------------------------------------------------------------------------------------------------------
room 要素
------------------------------------------------------------------------------------------------------------------------

room 要素は次の要素を持ちます。

id (必須項目)
    | 室の通し番号です。
    | boundary 要素が接する室や、換気経路の指定、機器を設置する室の指定などに使用されます。
    | 重複した番号は指定できません。
    | 数値（整数型）です。
    | 通常は、0番から順番につけてください。
name (必須項目)
    | 室の名称です。
    | 文字列型で設定してください。
    | プログラムではエラー表示等のみに使用し、計算には使用しません。
sub_name (必須項目)
    | 室の副名称です。
    | 文字列型で設定してください。
    | 使用しない場合は空の文字列 "" を指定する等してください。
    | プログラムではエラー表示等のみに使用し、計算には使用しません。
floor_area (必須項目)
    | 床面積です。
    | 数値（小数点型）で指定してください。単位は、 |m2| です。
volume (必須項目)
    | 気積です。
    | 数値（小数点型）で制定してください。単位は、 |m3| です。
ventilation (必須項目)
    | 換気量に関する設定です。
    | 現在、自然換気を表す natural 要素のみを持ちます。
    | なお、局所換気量は別途 csv 等のスケジュールで指定します。
    | 局所換気以外の機械換気は、別途 mechanical_ventilations 要素で指定します。
furniture (必須項目)
    | 家具等の室内の備品に関する設定です。
    | furniture 要素を持ちます。
schedule (必須項目)
    | スケジュールに関する設定です。
    | schedule 要素を持ちます。

ventilation 要素は次の要素を持ちます。

natural (必須項目)
    | 自然風利用時の換気量です。単位は |m3| / h です。
    | 本プログラムは室内間の自然風利用時の換気による空気移動は考慮しておりません。
    | 常に、室と外気とで空気移動を考慮します。

furniture 要素は次の要素を持ちます。

input_method (必須項目)
    | 家具等の室内の備品の仕様の指定方法です。default と specify が用意されています。
    | default が指定された場合は、室の気積に基づいて自動的に設定されます。
    | specify が指定された場合は、自分で仕様を指定します。
heat_capacity
    | 備品等の熱容量です。imput_method に specify が指定された場合のみ指定します。単位は J / K です。
    | 数値（小数点型）で指定します。
heat_cond
    | 空気と備品等間の熱コンダクタンスです。imput_method に specify が指定された場合のみ指定します。単位は W / K です。
    | 数値（小数点型）で指定します。
moisture_capacity
    | 備品等の湿気容量です。imput_method に specify が指定された場合のみ指定します。単位は kg / ( kg / kg(DA) ) です。
    | 数値（小数点型）で指定します。
moisture_cond
    | 空気と備品等間の湿気コンダクタンスです。imput_method に specify が指定された場合のみ指定します。単位は kg / ( s ( kg / kg(DA)) ) です。
    | 数値（小数点型）で指定します。

schedule 要素は次の要素を持ちます。

name (必須項目)
    | 室で指定されるスケジュール名称です。
    | スケジュールは「平日」「休日在宅」「休日外出」などの日毎に定義される日別スケジュールと、居住者人数 1人・2人・3人・4人ごとに決められており、別途 json 形式で保存・定義されています。
    | ここで指定する名称とスケジュール json のファイル名称は一致しておく必要があります。
    | スケジュール json ファイルの形式は別途、スケジュール json ファイルの説明の箇所を参照してください。

.. code-block::
    :caption: room 要素の記述例（家具等の備品を指定しない場合）

    {
        ...
        "rooms": [
            {
                "id": 0,
                "name": "living_room",
                "sub_name": "calc_pattern_0",
                "floor_area": 29.81,
                "volume": 70.92,
                "ventilation": {
                    "natural": 354.6
                },
                "furniture": {
                    "input_method": "default"
                },
                "schedule": {
                    "name": "main_occupant_room"
                }
            },
            ...
        ],
        ...
    }

.. code-block::
    :caption: room 要素の記述例（家具等の備品を指定する場合）

    {
        ...
        "rooms": [
            {
                "id": 0,
                "name": "living_room",
                "sub_name": "calc_pattern_0",
                "floor_area": 29.81,
                "volume": 70.92,
                "ventilation": {
                    "natural": 354.6
                },
                "furniture": {
                    "input_method": "specify",
                    "heat_capacity": 378000.0,
                    "heat_cond": 85.0,
                    "moisture_capacity": 500.0,
                    "moisture_cond": 0.9
                },
                "schedule": {
                    "name": "main_occupant_room"
                }
            },
            ...
        ],
        ...
    }

------------------------------------------------------------------------------------------------------------------------
boundary 要素
------------------------------------------------------------------------------------------------------------------------

boundary 要素は境界の仕様を表し、次の要素を持ちます。
なお、ここで境界と呼ぶのは、一般的な外皮（壁・屋根・外気床・界床・界壁）に加え、室と室（基礎断熱住宅の場合の床下空間も含む）との間の間仕切り壁・間仕切り床も含みます。

また、間仕切りの指定は、本プログラムでは少し特殊な設定となっています。
間仕切りの両側に位置する室をA、反対側の室をBとします。
本プログラムでは室Aから見た間仕切りと、室Bから見た間仕切りを別々に定義しないといけません。
間仕切りは実際の世界では1つだったとしても、本プログラムでは boudary 要素として室Aから見た情報と室Bから見た情報の2通りを指定しないといけません。
また、室Aから見た間仕切りと室Bから見た間仕切りは、見る方向が異なることで本来同じものですから、後述する層構成はちょうどリバースの関係になります。これも正しく入力する必要があります。

id (必須項目)
    | 境界の通し番号です。 
    | 境界が間仕切りの場合は、裏面の間仕切り番号を指定する場合に使用します。
    | 重複した番号は指定できません。
    | 数値（整数型）です。
    | 通常は、0番から順番につけてください。
name (必須項目)
    | 境界の名称です。
    | 文字列型で設定してください。
    | プログラムではエラー表示等のみに使用し、計算には使用しません。
sub_name (必須項目)
    | 境界の副名称です。
    | 文字列型で設定してください。
    | 使用しない場合は空の文字列 "" を指定する等してください。
    | プログラムではエラー表示等のみに使用し、計算には使用しません。
connected_room_id (必須項目)
    | 境界が接する室のIDです。
    | 別途 room 要素で定めた ID を指定します。room 要素に定めた ID 以外の値を指定するとエラーになります。
    | 数値（整数型）で指定します。
boundary_type (必須項目)
    | 境界の種類です。
    | "internal", "external_general_part", "external_transparent_part", "external_opaque_part", "ground" の中から1つを文字列で指定します。
    | "internal" とは、間仕切りのことです。
    | "external_general_part" とは、一般的な外皮のことを指し、開口部と地盤以外の外皮全般を指します。
    | "external_transparent_part" とは、透明な開口部を指します。一般的なガラス窓がこれに該当する他、大部分が透明な框ドアなどもこれにあたります。
    | "external_opaque_part" とは、非透明な開口部を指します。一般的に見られる透明ではないドアや、透明では無い板窓などがこれに該当します。
    | "ground" とは、地盤を指します。基礎断熱住宅や床断熱住宅における玄関や浴室下部など熱的境界が地盤と接する場合に指定します。なお、土間床周辺部の熱損失は別途指定します。
area (必須項目)
    | 境界の面積です。単位は |m2| です。数値（小数点型）で指定します。
is_sun_striked_outside
    | 外皮に日射があたるかどうかを指定します。
    | boundary_type が external_general_part, external_transparent_part, external_opaque_part の場合のみ指定します。
    | bool値で指定します。
    | true を指定した場合は、外皮の室外側表面に日射があたる設定となります。
temp_dif_coef
    | 温度差係数を表します。
    | boundary_type が external_general_part, external_transparent_part, external_opaque_part の場合のみ指定します。
    | 0.0から1.0までの間の数値（小数点型）で指定します。
    | 一般的に外気に接する場合は 1.0 を指定しますが、例えば、外気が床下空間、ピット、熱的に空調された空間などの場合は、例えば、0.0 や 0.7 等の数値が指定されます。
    | 外気の種類と指定する温度差係数の関係について詳しくは建築物省エネ法を参照してください。
rear_surface_boundary_id
    | 間仕切りの場合の裏面の境界のIDを指定します。
    | "boundary_type" が "internal" の場合のみ指定します。
    | 数値（整数型）で指定します。
    | 詳しい設定の方法は後述します。
is_solar_absorbed_inside (必須項目)
    | 開口部等を通して入ってきた日射の大部分は家具等の備品により吸収され、残りは室内側の境界に吸収されます。
    | この項目は、室内に入ってきた日射が当該境界で吸収されるか否かを指定します。
    | bool値で指定します。
    | 1つの室に複数の境界でこの項目が true になった場合は、入ってきた日射はその境界の面積に応じて按分されます。
is_floor (必須項目)
    | 当該境界が床かどうかを表します。
    | bool値で指定します。
    | 在室者と境界表面との放射のやり取りを計算する際に必要な、在室者との形態係数を計算する時のみに使用されます。
    | 在室者は通常、室中央よりも床に近いところに居ることを考慮して、本プログラムでは床の形態係数を少し大きめに評価しています。その際の計算に使用されます。
direction
    | 境界の向く向きを表します。
    | "is_sun_striked_outside" が true の場合のみ、指定します。
    | "s", "sw", "w", "nw", "n", "ne", "e", "se", "top", "bottom" の中から文字列で指定します。
    | "s", "sw", "w", "nw", "n", "ne", "e", "se" は、順に、南・南西・西・北西・北・北東・東・南東を表します。
    | "top" は上向き、"bottom" は下向きを表します。
    | 方位は8方位で指定することとしており、微妙な角度を指定することには対応していませんので、一番近い方位から選んでください。
    | また、水平方向または垂直方向に向いた外皮以外（例えば、傾斜屋根など）には対応していませんので、屋根の場合は "top"、壁の場合は方位から選ぶ等、近い向きを選んでください。
h_c (必須項目)
    | 室内側対流熱伝達率を表します。単位は W / ( |m2| K ) です。
    | 数値（小数点型）で指定します。
outside_emissivity
    | 室外側長波長放射率を表します。
    | boundary_type が external_general_part, external_transparent_part, external_opaque_part の場合のみ指定します。
    | 単位は無次元で、0.0から1.0の間の値を数値（小数点型）で指定します。
outside_heat_transfer_resistance
    | 室外側熱伝達抵抗を表します。
    | boundary_type が external_general_part, external_transparent_part, external_opaque_part の場合のみ指定します。
    | 単位は、 |m2| K / W で、数値（小数点型）で指定します。
eta_value
    | （垂直入射時の）日射熱取得率を表します。建具の影響を含んだ値です。
    | boundary_type が external_transparent_part の場合のみ指定します。
    | いわゆる、窓のη値であり、単位は無次元で、0.0から1.0の間の値を数値（小数点型）で指定します。
u_value
    | 熱貫流率を表します。建具の影響を含んだ値です。
    | boundary_type が external_transparent_part, external_opaque_part の場合のみ指定します。
    | 単位は、 W / ( |m2| K ) で、数値（小数点型）で指定します。
    | 一般的に開口部は、製造者がJIS等で定められた方法によって熱貫流率を計測・計算するためにこの項目を設けています。
    | 開口部以外の一般的な壁などの場合は、別途、層構成なども考慮して、spec 要素で指定します。
inside_heat_transfer_resistance
    | 室内側熱伝達抵抗を表します。
    | boundary_type が external_transparent_part, external_opaque_part の場合のみ指定します。
    | 単位は、 |m2| K / W で、数値（小数点型）で指定します。
    | ここで指定する室内側熱伝達抵抗は、室内の空気や境界の表面間の熱バランスの計算には使いません。
    | 熱バランスの計算に使われる熱伝達率のうち、室内側表面の放射熱伝達率は室内側の境界の面積から形態係数を推定して決められます。
    | 室内側表面の対流熱伝達率は、別途定める値 "h_c" です。
    | ここで定める室内側熱伝達抵抗は、窓やドアのカタログ値（U値）から表面熱伝達抵抗を取り除いた実質部（室内側表面から室外側空気まで）の熱抵抗を推定するのに使用されます。
glass_area_ratio
    | 開口部の面積に対するグレージングの面積の比率です。
    | boundary_type が external_transparent_part の場合のみ指定します。
    | 単位は無次元で、0.0から1.0の数値（小数点型）で指定します。
incident_angle_characteristics
    | 一般的に窓に入射する太陽光の入射角特性は窓のガラス構成によって大きく異なります。
    | 本計算プログラムではガラスの透過・反射等の計算を単純化するために、「単層ガラス」と「複層ガラス」に類型化して計算方法を用意しています。
    | boundary_type が external_transparent_part の場合のみ指定します。
    | "single", "multiple" のいずれかを指定します。
    | "single" とは単層ガラスを指します。
    | "multiple" とは複層ガラスを指します。
outside_solar_absorption
    | 室外側日射吸収率を表します。
    | boundary_type が external_general_part, external_opaque_part の場合のみ指定します。
    | 透明な開口部における日射吸収率は別途指定するη値から推定されるため、ここでの指定は不要です。
    | 単位は無次元で、0.0から1.0の数値（小数点型）で指定します。
layers
    | 開口部を除く外皮および地盤を構成する層を表します。
    | layer 要素のリストです。
    | "boundary_type" が "internal", "external_general_part", "ground" の場合のみ指定します。
    | "connected_room_id" で指定した室から順番にリスト構造で Layer 要素を並べる必要があります。
    | この layer 要素には、表面熱伝達抵抗を含める必要はありませんが、中空層などの空気層は含める必要があります。
solar_shading_part
    | 日除けの仕様を指定するための solar_shading_part 要素です。必須項目です。
    | "is_sun_striked_outside" が true の場合のみ、指定します。

以下、"boundary_type" ごとに、必要な要素が違うため、"boundary_type" ごとに記述例を示します。

.. code-block::
    :caption: 一般的な外皮("boundary_type" == "external_general_part")の boundary 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                "id": 1,
                "name": "LDK_south_wall",
                "sub_name": "for_test",
                "connected_room_id": 0,
                "boundary_type": "external_general_part",
                "area": 5.0,
                "is_sun_striked_outside": true,
                "temp_dif_coef": 1.0,
                "is_solar_absorbed_inside": false,
                "is_floor": false,
                "direction": "s",
                "h_c": 2.5,
                "outside_emissivity": 0.9,
                "outside_heat_transfer_resistance": 0.04,
                "outside_solar_absorption": 0.8,
                "layer": [
                    ...
                ],
                "solar_shading_part": {
                    ...
                }
            },
            {
                ...
            },
            ...
        ],
        ...
    }

.. code-block::
    :caption: 透明な開口部("boundary_type" == "external_transparent_part")の boundary 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                "id": 6,
                "name": "kitchen_window_east",
                "sub_name": "for_test",
                "connected_room_id": 1,
                "boundary_type": "external_transparent_part",
                "area": 5.0,
                "is_sun_striked_outside": true,
                "temp_dif_coef": 1.0,
                "is_solar_absorbed_inside": false,
                "is_floor": false,
                "direction": "e",
                "h_c": 2.5,
                "outside_emissivity": 0.9,
                "outside_heat_transfer_resistance": 0.04,
                "eta_value": 0.8,
                "u_value": 4.65,
                "inside_heat_transfer_resistance": 0.11,
                "glass_area_ratio": 0.8,
                "incident_angle_characteristics": "multiple",
                "solar_shading_part": {
                    ...
                }
            },
            {
                ...
            },
            ...
        ],
        ...
    }


.. code-block::
    :caption: 非透明な開口部("boundary_type" == "external_opaque_part")の boundary 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                "id": 10,
                "name": "entrance_door",
                "sub_name": "for_test",
                "connected_room_id": 8,
                "boundary_type": "external_opaque_part",
                "area": 2.0,
                "is_sun_striked_outside": true,
                "temp_dif_coef": 1.0,
                "is_solar_absorbed_inside": false,
                "is_floor": false,
                "direction": "w",
                "h_c": 2.5,
                "outside_emissivity": 0.9,
                "outside_heat_transfer_resistance": 0.04,
                "u_value": 4.65,
                "inside_heat_transfer_resistance": 0.11,
                "outside_solar_absorption": 0.8,
                "solar_shading_part": {
                    ...
                }
            },
            {
                ...
            },
            ...
        ],
        ...
    }

.. code-block::
    :caption: 間仕切り("boundary_type" == "internal")の boundary 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                "id": 17,
                "name": "LDK_hall_inside_wall",
                "sub_name": "for_test",
                "connected_room_id": 0,
                "boundary_type": "internal",
                "area": 10.0,
                "rear_surface_boundary_id": 5,
                "is_solar_absorbed_inside": false,
                "is_floor": false,
                "h_c": 2.5,
                "layer": [
                    ...
                ]
            },
            {
                ...
            },
            ...
        ],
        ...
    }

.. code-block::
    :caption: 地盤("boundary_type" == "ground")の boundary 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                "id": 21,
                "name": "hall_earth_floor",
                "sub_name": "for_test",
                "connected_room_id": 7,
                "boundary_type": "ground",
                "area": 10.0,
                "is_solar_absorbed_inside": false,
                "is_floor": true,
                "h_c": 2.5,
                "layer": [
                    ...
                ]
            },
            {
                ...
            },
            ...
        ],
        ...
    }

ここで、間仕切りの場合、間仕切りの両側の室を室Aと室Bとすると、室A側から見た間仕切りと室B側から見た間仕切りの両方を入力しないといけません。
また、裏面の境界のIDとしてお互いの間仕切りを指定しないといけません。

例えば、
室AがLDK、室Bがホールだとして、その室IDが、1と15だったとします。
LDKとホールの間の間仕切りは、LDK側から見た間仕切りとホールから見た間仕切りとして、同じ間仕切りを2つ登録しないといけません。
LDKから見た間仕切りのIDを7、ホールから見た間仕切りを8とします。

.. code-block::
    :caption: LDKとホールとの間の間仕切りの記述例

    {
        ...
        "rooms": [
            {
                "id": 1,
                "name": "LDK",
                ...
            },
            ...
            {
                "id": 15,
                "name": "hall",
                ...
            },
            ...
        ],
        "boundaries": [
            ...
            {
                "id": 7,
                "name": "LDK-hall LDK side",
                "connected_room_id": 1,
                "boundary_type": "internal",
                ...
                "rear_surface_boundary_id": 8,
                ...
            },
            {
                "id": 8,
                "name": "LDK-hall hall side",
                "connected_room_id": 15,
                "boundary_type": "internal",
                ...
                "rear_surface_boundary_id": 7,
                ...
            },
            ...
        ],
        ...
    }

このように、1つの間仕切りを必ず2つ指定し、かつ、"rear_surface_boundary_id"には、それぞれお互いのIDを指定しなければなりません。

------------------------------------------------------------------------------------------------------------------------
layer 要素
------------------------------------------------------------------------------------------------------------------------

間仕切り・一般的な外皮・地盤における層構成を表します。
手前側（"connected_room_id"で指定した室側）から向こう側（"boundary_type"が"internal"以外の場合は室内側から室外側）に向けて記載します。

name (必須項目)
    | 層の名称です。（計算では使用しません。）
thermal_resistance (必須項目)
    | 熱抵抗です。単位は、 |m2| K / W です。
    | 0 より大きい数値（小数点型）で指定します。
thermal_capacity (必須項目)
    | 単位面積あたりの熱容量です。単位は、 kJ / |m2| K です。
    | 0 以上の数値（小数点型）で指定します。

.. code-block::
    :caption: layers 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                ...
                "layers": [
                    {
                        "name": "plaster_board",
                        "thermal_resistance": 0.0432,
                        "thermal_capacity": 7.885
                    },
                    ...
                ],
                ...
            },
            {
                ...
            }
        ],
        ...
    }

間仕切りの場合は、前述した例で説明すると、室A側から見た層構成と室B側から見た層構成の順番はちょうど逆になっていないといけません。

地盤の場合は、地盤を覆うコンクリートやモルタル、タイル、断熱材、など、地盤を除く材料を記述します。
地盤は含める必要はありません。

------------------------------------------------------------------------------------------------------------------------
solar_shading_part 要素
------------------------------------------------------------------------------------------------------------------------

日除けの仕様を定義します。
"is_sun_striked_outside" が true の場合のみ定義されます。

existence (必須項目)
    | 日除けの有無
    | bool型で定義します。
    | 本プログラムでは日除けは垂直壁・開口部のみに定義できます。従って、傾斜屋根等の垂直でない外皮が有する日除けについては、ここで日除けの有無は無しと定義してください。
input_method
    | 日除けの入力方法です。"existence" が true の場合のみ定義されます。
    | "simple", "detail" のいずれかを設定します。
    | "simple" とは簡易入力を意味します。本入力方法はオーバーハング型の日除けのみ評価可能であり、日除けの形状は深さのみ指定可能で、横方向の長さは指定できません。
    | "detail" とは詳細入力を意味します。本入力方法はオーバーハング型とサイドフィン型の日除けのいずれかまたは両方が評価可能です。日除けの深さに加えて横・縦方向の長さも指定できます。
depth
    | 日除けの深さです。"input_method" が "simple" の場合のみ定義します。
    | 単位は、 m です。
    | 数値（小数点型）で指定します。
d_h
    | 日除けが対象とする外皮の部位の高さ方向の長さです。"input_method" が "simple" の場合のみ定義します。
    | 開口部の場合は開口部の高さを表します。
    | 壁の場合は壁の高さ方向の長さを表します。
    | 単位は m です。
    | 数値（小数点型）で指定します。
d_e
    | 日除けが対象とする外皮の部位と日除けの付け根との距離を表します。"input_method" が "simple" の場合のみ定義します。
    | 開口部の場合は開口部上端から日除けの付け根までの高さ方向の距離となります。
    | 壁の場合は通常この値はゼロとなりますが、壁を細かく区切って、対象となる壁と日除けが離れている場合は開口部と同様に入力します。
    | 単位は m です。
    | 数値（小数点型）で指定します。
x_1
    | オーバーハング型の日除けの横方向の長さです。
    | 開口部からはみ出た長さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
x_2
    | 開口部の横方向の長さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
x_3
    | オーバーハング型の日除けの横方向の長さです。
    | 開口部からはみ出た長さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
y_1
    | サイドフィン型の日除けの縦方向の長さです。
    | 開口部から上側にはみ出た長さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
y_2
    | 開口部の縦方向の長さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
y_3
    | サイドフィン型の日除けの縦方向の長さです。
    | 開口部から上側にはみ出た長さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
z_x_pls
    | サイドフィン型の日除けの深さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
z_x_mns
    | サイドフィン型の日除けの深さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
z_y_pls
    | 上ひさしの日除けの深さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。
z_y_mns
    | 下ひさしの日除けの深さです。
    | 単位は m です。
    | 数値（小数点型）で指定します。

.. code-block::
    :caption: 日除けが無い場合のsolar_shading_part 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                ...
                "solar_shading_part": {
                    "existence": false
                }
            },
            {
                ...
            }
        ],
        ...
    }

.. code-block::
    :caption: 日除けがある場合で簡易入力をする場合のsolar_shading_part 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                ...
                "solar_shading_part": {
                    "existence": true,
                    "input_method": "simple",
                    "depth": 1.0,
                    "d_h": 2.1,
                    "d_e": 0.5
                }
            },
            {
                ...
            }
        ],
        ...
    }

.. code-block::
    :caption: 日除けがある場合で詳細入力をする場合のsolar_shading_part 要素の記述例

    {
        ...
        "boundary": [
            {
                ...
            },
            {
                ...
                "solar_shading_part": {
                    "existence": true,
                    "input_method": "detail",
                    "x1": 0.1,
                    "x2": 2.5,
                    "x3": 0.1,
                    "y1": 0.4,
                    "y2": 2.3,
                    "y3": 0.0,
                    "z_x_pls": 0.3,
                    "z_x_mns": 0.3,
                    "z_y_pls": 0.4,
                    "z_y_mns": 1.0
                }
            },
            {
                ...
            }
        ],
        ...
    }

------------------------------------------------------------------------------------------------------------------------
mechanical_ventilation 要素
------------------------------------------------------------------------------------------------------------------------

機械換気の経路を指定します。

ID (必須項目)
    | 機械換気の経路のIDです。
    | 数値（整数型）で指定します。
root_type (必須項目)
    | 機械換気の経路のタイプを表します。
    | "type1", "type2", "type3" のいずれかを選択します。
    | "type1" は第一種換気を表します。
    | "type2" は第二種換気を表します。
    | "type3" は第三種換気を表します。
volume (必須項目)
    | 換気量です。単位は |m3| / h です。
    | 数値（小数点型）で指定します。
route (必須項目)
    | 換気経路上の室のIDをリストで指定します。
    | 換気経路の始点と終点は必ず外気になります。
    | 例えば、外気→室0→室5→外気 というように空気が流れる場合は、始点と終点の外気は省き、[0, 5] のように記述します。
    | 数値（整数型）のリストで表します。

.. code-block::
    :caption: mechanical_ventilation 要素の記述例

    {
        ...
        "mechanical_ventilations": [
            {...},
            {
                ...
                "id": 0,
                "root_type": "type3",
                "volume": 60.0,
                "route": [0, 5]
            },
            {...}
        ],
        ...
    }

