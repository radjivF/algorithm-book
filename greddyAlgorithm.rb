moneyDollars= [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01]

def greedyMethod(whichDollar, giveback)
  if giveback == 0
    puts("done")
  else
    while(giveback <= moneyDollars[whichDollar])
      giveback -= moneyDollars[whichDollar]
      puts (moneyDollars[whichDollar])
    end
    whichDollar -= 1
    greedyMethod(whichDollar ,giveback)
  end
end

greddyMethod(moneyDollars.length, 263 )
