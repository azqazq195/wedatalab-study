package org.example.week1_dp.`1로_2만들기_2`

import java.io.ByteArrayInputStream
import java.util.*

fun main() {
    val testInput = "10"
    System.setIn(ByteArrayInputStream(testInput.toByteArray()))

    val reader = System.`in`.bufferedReader()
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()

    val dp = IntArray(n + 1)
    val trace = IntArray(n + 1)

    for (i in 2..n) {
        dp[i] = dp[i - 1] + 1
        trace[i] = i - 1
        if (i % 2 == 0 && dp[i] > dp[i / 2] + 1) {
            dp[i] = dp[i / 2] + 1
            trace[i] = i / 2
        }
        if (i % 3 == 0 && dp[i] > dp[i / 3] + 1) {
            dp[i] = dp[i / 3] + 1
            trace[i] = i / 3
        }
    }

    println(dp[n])
    val sb = StringBuilder()
    var i = n
    while (i > 0) {
        sb.append("$i ")
        i = trace[i]
    }
    println(sb)

    reader.close()
}
