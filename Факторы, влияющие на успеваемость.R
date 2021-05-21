install.packages("ggplot2")

library(ggplot2)

data <- read.csv("C:/Users/Катя/Desktop/StudentsPerformance.csv")

str(data)
head(data, n=10)
#colnames(data)

#«пол» «расовая принадлежность» «родительский уровень образования» «обед»
#«курс подготовки к экзаменам» «оценка по математике» «оценка по чтению» «оценка по письму»

# Вопросы: 1. Есть ли зависимость между полом ученика и его оценками по мат/чтению/письму
#          2. Как связны образование родителей и оценка ученика
#          3. Есть ли влияние расовой принадлежности на успеваемость?



data$gender <- as.factor(data$gender)
data$race.ethnicity <- as.factor(data$race.ethnicity)
data$parental.level.of.education <- as.factor(data$parental.level.of.education)

########################

my_f <- function(x){
  x <- as.numeric(x)
  sum(x[c(6, 7, 8)])
}

res <- apply(data, 1, FUN = my_f)

data$total <- res

###################



# 1) Есть ли влияние пола на успеваемость по математике

by(data$math.score, INDICES = data$gender, shapiro.test)

# H0: пол не влияет на оценки учащихся по математике
t.test(data$math.score ~ data$gender)


ggplot(data, aes(x=gender, y=math.score, color=gender)) + 
  geom_boxplot() +
  labs(title="Сравнение оценок по математике в зависимости от пола",x="Пол ученика", y = "Оценка по математике")



# 2) Есть ли влияние пола на успеваемость по чтению
by(data$reading.score, INDICES = data$gender, shapiro.test)


t.test(data$reading.score ~ data$gender)


ggplot(data, aes(x=gender, y=reading.score, color=gender)) + 
  geom_boxplot() +
  labs(title="Сравнение оценок по чтению в зависимости от пола",x="Пол ученика", y = "Оценка по чтению")



# 3) Есть ли влияние пола на успеваемость по письму
by(data$writing.score, INDICES = data$gender, shapiro.test)

t.test(data$writing.score ~ data$gender)

ggplot(data, aes(x=gender, y=writing.score, color=gender)) + 
  geom_boxplot() +
  labs(title="Сравнение оценок по письму в зависимости от пола",x="Пол ученика", y = "Оценка по письму")


t.test(data$total ~ data$gender)

ggplot(data, aes(x=gender, y=total, color=gender)) + 
  geom_boxplot() +
  labs(title="Сравнение общего балла в зависимости от пола",x="Пол ученика", y = "Общий балл")






######################################

ggplot(data, aes(x=race.ethnicity, y=total, color=race.ethnicity)) + 
  geom_boxplot() +
  labs(title="Сравнение общего балла в зависимости от расовой принадлежности",x="Раса", y = "Общий балл")




data$factor_total <- ifelse(data$total > mean(data$total), 1, 0)


t <- table(data$factor_total, data$race.ethnicity)
# Н0: расовая принадлежность не влияет на общую успеваемость
chisq.test(t)
# p-value < 0.05, что позволяет отвергнуть нулевую гипотезу
# т.е. расовая принадлежность влияет на успеваемость


#####################################
data$parental.level.of.education <- factor(data$parental.level.of.education, 
                                           levels=c("master's degree",
                                                    "bachelor's degree",
                                                    "associate's degree",
                                                    "some college",
                                                    "some high school",
                                                    "high school"))

ggplot(data, aes(x=parental.level.of.education, y=total, color=parental.level.of.education)) + 
  geom_boxplot() +
  labs(title="Сравнение общего балла в зависимости от образования родителей",x="Образование", y = "Общий балл") +
  scale_x_discrete(guide = guide_axis(n.dodge = 2))

t <- table(data$factor_total, data$parental.level.of.education)
chisq.test(t)



ggplot(data, aes(x = reading.score, y = writing.score)) +
  geom_point() + 
  labs()

###################################

cor(data$reading.score, data$writing.score)

ggplot(data, aes(x = reading.score, y = writing.score, colour="red")) + 
  geom_point() + 
  labs(title="Диаграмма рассеяния между оценкой по письму и чтением", x= "Оценка по чтению", y = "Оценка по письму")


cor(data$writing.score, data$math.score)

ggplot(data, aes(x = writing.score, y = math.score, color="red")) + 
  geom_point() + 
  labs(title="Диаграмма рассеяния между оценкой по письму и математике",x="Оценка по письму", y = "Оценка по математике")



###################################
model <- lm(total ~ (gender + race.ethnicity + parental.level.of.education + lunch)^2, data = data)
summary(model)
