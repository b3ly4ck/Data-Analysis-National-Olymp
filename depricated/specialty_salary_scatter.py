import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter import filter_dataset
from scipy.stats import mannwhitneyu, spearmanr
from services.specialty_grouping import distribute_specialties
groups = {
        "Юристы": ['Юрисконсульт', 'Юрист'],
        "Финансы, бухгалтерия": ['Экономист', 'Финансовый менеджер', 'Кредитный специалист', 'Бухгалтер'],
        "Управление персоналом, тренинги": ['Менеджер по персоналу', 'Специалист по кадрам', 'Специалист по отбору персонала','Специалист по подбору персонала'],
        "Туризм, гостиницы, рестораны": ['Менеджер по туризму', 'Менеджер ресторана', 'Менеджер АХО', 'Официант, бармен, бариста','Повар, пекарь, кондитер','Уборщица, уборщик'],
        "Транспорт, логистика, перевозки": ['Упаковщик, комплектовщик', 'Руководитель отдела логистики', 'Начальник склада', 'Машинист', 'Менеджер по логистике, менеджер по ВЭД', 'Водитель', 'Диспетчер', 'Кладовщик', 'Курьер'],
        'Строительство, недвижимость': ['Сварщик', 'Слесарь, сантехник', 'Разнорабочий', 'Руководитель проектов', 'Монтажник', 'Инженер-конструктор, инженер-проектировщик', 'Инженер по охране труда и технике безопасности, инженер-эколог', 'Дизайнер, художник'],
        'Стратегия, инвестиции, консалтинг': ['Руководитель проектов', 'Аналитик'],
        'Спортивные клубы, фитнес, салоны красоты': ['Фитнес-тренер, инструктор тренажерного зала', 'Менеджер по продажам, менеджер по работе с клиентами'],
        'Сельское хозяйство': ['Сервисный инженер, инженер-механик', 'Технолог'],
        'Розничная торговля': ['Администратор магазина, администратор торгового зала', 'Мерчандайзер', 'Продавец-консультант, продавец-кассир', 'Супервайзер', 'Товаровед'],
        'Рабочий персонал': [ 'Кладовщик', 'Механик', 'Монтажник', 'Оператор производственной линии', 'Разнорабочий', 'Сварщик', 'Сервисный инженер, инженер-механик', 'Слесарь, сантехник', 'Упаковщик, комплектовщик'],
        'Производство, сервисное обслуживание': ['Инженер по охране труда и технике безопасности, инженер-эколог', 'Инженер-конструктор, инженер-проектировщик', 'Машинист', 'Механик', 'Начальник производства', 'Начальник смены, мастер участка', 'Оператор производственной линии', 'Сварщик', 'Сервисный инженер, инженер-механик', 'Слесарь, сантехник', 'Технолог'],
        'Продажи, обслуживание клиентов': [ 'Кассир-операционист', 'Координатор отдела продаж', 'Кредитный специалист', 'Менеджер по продажам, менеджер по работе с клиентами', 'Оператор call-центра, специалист контактного центра', 'Продавец-консультант, продавец-кассир', 'Руководитель отдела продаж', 'Специалист технической поддержки', 'Торговый представитель'],
        'Наука, Образование': [ 'Психолог', 'Учитель, преподаватель, педагог'],
        'Медицина, фармацевтика': ["Врач"],
        'Маркетинг, реклама, PR': ['SMM-менеджер, контент-менеджер', 'Аналитик', 'Дизайнер, художник', 'Менеджер по маркетингу, интернет-маркетолог', 'Менеджер по продажам, менеджер по работе с клиентами'],
        'Искусство, развлечения, массмедиа': ['Дизайнер, художник'],
        'Информационные технологии': ['Аналитик', 'Дизайнер, художник', 'Программист, разработчик', 'Руководитель проектов', 'Системный администратор', 'Тестировщик'],
        'Домашний, обслуживающий персонал': [ 'Воспитатель, няня', 'Курьер', 'Охранник', 'Уборщица, уборщик'],
        'Высший и средний менеджмент': ['Генеральный директор, исполнительный директор (CEO)', 'Начальник производства',  'Директор магазина, директор сети магазинов'],
        'Закупки': ["Менеджер по закупкам"],
        "Безопасность": ["Охранник"],
        'Административный персонал': ['Администратор', 'Делопроизводитель, архивариус', 'Менеджер/руководитель АХО', 'Оператор ПК, оператор базы данных', 'Офис-менеджер', 'Секретарь, помощник руководителя, ассистент']
    }
specialties = groups.keys()
df = pd.read_csv('../hh_ru_dataset.csv', sep=',')
df["age"] = df["year_of_birth"].apply(lambda x: 2023 - x)
df['age_category'] = df["year_of_birth"].apply(
    lambda x: f"{str((2023 - x) // 10 * 10)}-{str((2023 - x) // 10 * 10 + 10)}")
df = filter_dataset(df)
fig, ax = plt.subplots(figsize=(7, 7))
fig = sns.barplot(x="average_salary", y="specialty", data=res, hue="age_group", color="#FFF465", orient="y")
fig = ax.get_figure()
plt.rc('xtick', labelsize=40)
plt.rc('ytick', labelsize=40)
plt.ylabel("Специальность")
plt.xlabel("Средняя зарплата")
plt.tight_layout()
ax.get_legend().remove()
fig.savefig("charts_final/" + "Средняя зарплата от специальности" + '.png', transparent=True)
print(res)
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
           markers=["o", "x"], palette="Set1");