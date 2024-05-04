package org.example.week1_dp.LCS

import java.io.ByteArrayInputStream
import kotlin.math.max

fun main() {
    val testInput = """
        ACAYKP
        CAPCAK
    """.trimIndent()
    System.setIn(ByteArrayInputStream(testInput.toByteArray()))

    val reader = System.`in`.bufferedReader()
    val n = reader.readLine()
    val m = reader.readLine()

    val dp = Array(n.length + 1) { IntArray(m.length + 1) }
    for (i in 1..n.length) {
        for (k in 1..m.length) {
            if (n[i - 1] == m[k - 1]) {
                dp[i][k] = dp[i - 1][k - 1] + 1
            } else {
                dp[i][k] = max(dp[i-1][k], dp[i][k - 1])
            }

        }
    }

    println(dp[n.length][m.length])

    reader.close()
}