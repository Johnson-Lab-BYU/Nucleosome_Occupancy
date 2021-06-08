library(ggplot2)

CSV <- read.csv(readline(prompt="Enter csv file: "), fileEncoding="UTF-8-BOM")

ggplot(data=CSV, aes(x = Position)) +
  geom_line(aes(y = Score)) +
  #geom_ribbon(aes(y = Score*2, xmin=-56, xmax=-51), fill="turquoise1", alpha=0.35)+
  geom_ribbon(aes(y = Score*2, xmin=-45, xmax=45), fill="cornflowerblue", alpha=0.35)+
  geom_ribbon(aes(y = Score*2, xmin=50, xmax=61), fill="navy", alpha=0.35)+
  theme_minimal() +
  ylab("Positioning Score") +
  xlab("Position") +
  ylim(0, .5)
