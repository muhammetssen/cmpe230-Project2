for currentCount in {1..13}
do
    echo "Testcase $currentCount"
    python3 assembler/cpu230assemble.py inputs/input$currentCount.asm
    # python3 executer/cpu230execute.py inputs/input$currentCount.bin > cat.txt
    diff -s --strip-trailing-cr outputs/output$currentCount.txt <(python3 executer/cpu230exec.py inputs/input$currentCount.bin)
done
