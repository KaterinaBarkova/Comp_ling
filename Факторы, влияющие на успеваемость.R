install.packages("ggplot2")

library(ggplot2)

data <- read.csv("C:/Users/����/Desktop/StudentsPerformance.csv")

str(data)
head(data, n=10)
#colnames(data)

#���� �������� ��������������� ������������� ������� ������������ �����
#����� ���������� � ��������� ������� �� ���������� ������� �� ������� ������� �� ������

# �������: 1. ���� �� ����������� ����� ����� ������� � ��� �������� �� ���/������/������
#          2. ��� ������ ����������� ��������� � ������ �������
#          3. ���� �� ������� ������� �������������� �� ������������?



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



# 1) ���� �� ������� ���� �� ������������ �� ����������

by(data$math.score, INDICES = data$gender, shapiro.test)

# H0: ��� �� ������ �� ������ �������� �� ����������
t.test(data$math.score ~ data$gender)


ggplot(data, aes(x=gender, y=math.score, color=gender)) + 
  geom_boxplot() +
  labs(title="��������� ������ �� ���������� � ����������� �� ����",x="��� �������", y = "������ �� ����������")



# 2) ���� �� ������� ���� �� ������������ �� ������
by(data$reading.score, INDICES = data$gender, shapiro.test)


t.test(data$reading.score ~ data$gender)


ggplot(data, aes(x=gender, y=reading.score, color=gender)) + 
  geom_boxplot() +
  labs(title="��������� ������ �� ������ � ����������� �� ����",x="��� �������", y = "������ �� ������")



# 3) ���� �� ������� ���� �� ������������ �� ������
by(data$writing.score, INDICES = data$gender, shapiro.test)

t.test(data$writing.score ~ data$gender)

ggplot(data, aes(x=gender, y=writing.score, color=gender)) + 
  geom_boxplot() +
  labs(title="��������� ������ �� ������ � ����������� �� ����",x="��� �������", y = "������ �� ������")


t.test(data$total ~ data$gender)

ggplot(data, aes(x=gender, y=total, color=gender)) + 
  geom_boxplot() +
  labs(title="��������� ������ ����� � ����������� �� ����",x="��� �������", y = "����� ����")






######################################

ggplot(data, aes(x=race.ethnicity, y=total, color=race.ethnicity)) + 
  geom_boxplot() +
  labs(title="��������� ������ ����� � ����������� �� ������� ��������������",x="����", y = "����� ����")




data$factor_total <- ifelse(data$total > mean(data$total), 1, 0)


t <- table(data$factor_total, data$race.ethnicity)
# �0: ������� �������������� �� ������ �� ����� ������������
chisq.test(t)
# p-value < 0.05, ��� ��������� ���������� ������� ��������
# �.�. ������� �������������� ������ �� ������������


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
  labs(title="��������� ������ ����� � ����������� �� ����������� ���������",x="�����������", y = "����� ����") +
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
  labs(title="��������� ��������� ����� ������� �� ������ � �������", x= "������ �� ������", y = "������ �� ������")


cor(data$writing.score, data$math.score)

ggplot(data, aes(x = writing.score, y = math.score, color="red")) + 
  geom_point() + 
  labs(title="��������� ��������� ����� ������� �� ������ � ����������",x="������ �� ������", y = "������ �� ����������")



###################################
model <- lm(total ~ (gender + race.ethnicity + parental.level.of.education + lunch)^2, data = data)
summary(model)
