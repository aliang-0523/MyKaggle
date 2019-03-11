import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import sklearn.preprocessing as preprocessing
from sklearn import linear_model
from sklearn.ensemble import BaggingRegressor

data_train=pd.read_csv('F:/Kaggle/titanic/train_lanechange.csv')

'''
���ӻ��۲�����
'''
# fig = plt.figure()
# fig.set(alpha=0.2)  # �趨ͼ����ɫalpha����
#
# plt.subplot2grid((2,3),(0,0))             # ��һ�Ŵ�ͼ����м���Сͼ
# data_train.Survived.value_counts().plot(kind='bar')# ��״ͼ
# plt.title(u"������ (1Ϊ���)") # ����
# plt.ylabel(u"����")
#
# plt.subplot2grid((2,3),(0,1))
# data_train.Pclass.value_counts().plot(kind="bar")
# plt.ylabel(u"����")
# plt.title(u"�˿͵ȼ��ֲ�")
#
# plt.subplot2grid((2,3),(0,2))
# plt.scatter(data_train.Survived, data_train.Age)
# plt.ylabel(u"����")                         # �趨����������
# plt.grid(b=True, which='major', axis='y')
# plt.title(u"�����俴��ȷֲ� (1Ϊ���)")
#
#
# plt.subplot2grid((2,3),(1,0), colspan=2)
# data_train.Age[data_train.Pclass == 1].plot(kind='kde')
# data_train.Age[data_train.Pclass == 2].plot(kind='kde')
# data_train.Age[data_train.Pclass == 3].plot(kind='kde')
# plt.xlabel(u"����")# plots an axis lable
# plt.ylabel(u"�ܶ�")
# plt.title(u"���ȼ��ĳ˿�����ֲ�")
# plt.legend((u'ͷ�Ȳ�', u'2�Ȳ�',u'3�Ȳ�'),loc='best') # sets our legend for our graph.
#
#
# plt.subplot2grid((2,3),(1,2))
# data_train.Embarked.value_counts().plot(kind='bar')
# plt.title(u"���Ǵ��ڰ��ϴ�����")
# plt.ylabel(u"����")
# plt.show()
# fig = plt.figure()
# fig.set(alpha=0.2)  # �趨ͼ����ɫalpha����
#
# Survived_0 = data_train.Pclass[data_train.Survived == 0].value_counts()
# Survived_1 = data_train.Pclass[data_train.Survived == 1].value_counts()
# df=pd.DataFrame({u'���':Survived_1, u'δ���':Survived_0})
# df.plot(kind='bar', stacked=True)
# plt.title(u"���˿͵ȼ��Ļ�����")
# plt.xlabel(u"�˿͵ȼ�")
# plt.ylabel(u"����")
# plt.show()
# fig = plt.figure()
# fig.set(alpha=0.2)  # �趨ͼ����ɫalpha����
#
# Survived_0 = data_train.Embarked[data_train.Survived == 0].value_counts()
# Survived_1 = data_train.Embarked[data_train.Survived == 1].value_counts()
# df=pd.DataFrame({u'���':Survived_1, u'δ���':Survived_0})
# df.plot(kind='bar', stacked=True)
# plt.title(u"����¼�ۿڳ˿͵Ļ�����")
# plt.xlabel(u"��¼�ۿ�")
# plt.ylabel(u"����")
#
# plt.show()
# fig = plt.figure()
# fig.set(alpha=0.2)  # �趨ͼ����ɫalpha����
#
# Survived_cabin = data_train.Survived[pd.notnull(data_train.Cabin)].value_counts()
# Survived_nocabin = data_train.Survived[pd.isnull(data_train.Cabin)].value_counts()
# df=pd.DataFrame({u'��':Survived_cabin, u'��':Survived_nocabin}).transpose()
# df.plot(kind='bar', stacked=True)
# plt.title(u"��Cabin���޿�������")
# plt.xlabel(u"Cabin����")
# plt.ylabel(u"����")
# plt.show()
'''
���ȱʧ����
'''
'''
def set_missing_ages(df):

    # �����е���ֵ������ȡ��������Random Forest Regressor��
    id_df = df[['id','Amp2_1', 'cha', 'E2', 'E','speed','change']]

    # �˿ͷֳ���֪�����δ֪����������
    known_id = id_df[id_df.id.notnull()].as_matrix()
    unknown_id = id_df[id_df.id.isnull()].as_matrix()

    # y��Ŀ������
    y = known_id[:, 0]

    # X����������ֵ
    X = known_id[:, 1:]

    # fit��RandomForestRegressor֮��
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)

    # �õõ���ģ�ͽ���δ֪������Ԥ��
    predictedIds = rfr.predict(unknown_id[:, 1::])

    # �õõ���Ԥ�����ԭȱʧ����
    df.loc[ (df.id.isnull()), 'id' ] = predictedIds

    return df, rfr
'''
'''
def set_Cabin_type(df):
    df.loc[ (df.Cabin.notnull()), 'Cabin' ] = "Yes"
    df.loc[ (df.Cabin.isnull()), 'Cabin' ] = "No"
    return df
'''

#data_train, rfr = set_missing_ages(data_train)
#data_train = set_Cabin_type(data_train)
'''
�������ӻ�
'''
dummies_change = pd.get_dummies(data_train['change'], prefix= 'change')
df = pd.concat([data_train, dummies_change], axis=1)
df.drop(['id','change'], axis=1, inplace=True)
df
'''
��һ��
'''
scaler = preprocessing.StandardScaler()
#df['Age'].values.reshape(-1,1)��Age����ֵת��Ϊ������
Amp2_1_scale_param = scaler.fit(df['Amp2_1'].values.reshape(-1,1))
df['Amp2_1_scaled'] = scaler.fit_transform(df['Amp2_1'].values.reshape(-1,1), Amp2_1_scale_param)
cha_scale_param = scaler.fit(df['cha'].values.reshape(-1,1))
df['cha_scaled'] = scaler.fit_transform(df['cha'].values.reshape(-1,1), cha_scale_param)
E2_scale_param = scaler.fit(df['E2'].values.reshape(-1,1))
df['E2_scaled'] = scaler.fit_transform(df['E2'].values.reshape(-1,1), E2_scale_param)
E_scale_param = scaler.fit(df['E'].values.reshape(-1,1))
df['E_scaled'] = scaler.fit_transform(df['E'].values.reshape(-1,1), E_scale_param)
df

'''
��ģ
'''
# ������ȡ������Ҫ������ֵ
train_df = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.as_matrix()

# y��Survival���
y = train_np[:, 0]

# X����������ֵ
X = train_np[:, 1:]

# fit��RandomForestRegressor֮��
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)

clf

'''
���Լ�����ͬ����
'''
data_test = pd.read_csv("F:/Kaggle/titanic/test.csv")
data_test.loc[ (data_test.Fare.isnull()), 'Fare'] = 0
# �������Ƕ�test_data����train_data��һ�µ������任
# ������ͬ����RandomForestRegressorģ�����϶�ʧ������
tmp_df = data_test[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]
null_age = tmp_df[data_test.Age.isnull()].as_matrix()
# ������������XԤ�����䲢����
X = null_age[:, 1:]
#predictedAges = rfr.predict(X)
data_test.loc[ (data_test.Age.isnull()), 'Age' ] = predictedAges

#data_test = set_Cabin_type(data_test)
dummies_Cabin = pd.get_dummies(data_test['Cabin'], prefix= 'Cabin')
dummies_Embarked = pd.get_dummies(data_test['Embarked'], prefix= 'Embarked')
dummies_Sex = pd.get_dummies(data_test['Sex'], prefix= 'Sex')
dummies_Pclass = pd.get_dummies(data_test['Pclass'], prefix= 'Pclass')

#concat������ֵ���й�һ��
df_test = pd.concat([data_test, dummies_Cabin, dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df_test.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
df_test['Age_scaled'] = scaler.fit_transform(df_test['Age'].values.reshape(-1,1), age_scale_param)
df_test['Fare_scaled'] = scaler.fit_transform(df_test['Fare'].values.reshape(-1,1), fare_scale_param)
df_test
'''
Ԥ����
'''
test = df_test.filter(regex='Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
predictions = clf.predict(test)
result = pd.DataFrame({'PassengerId':data_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
result.to_csv("F:/Kaggle/titanic/logistic_regression_predictions.csv", index=False)

'''
�߼�ģ�͹�������
'''
test=pd.DataFrame({"columns":list(train_df.columns)[1:], "coef":list(clf.coef_.T)})
df_test

'''
������֤
'''
from sklearn import cross_validation

 #�򵥿���������
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
all_data = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
X = all_data.as_matrix()[:,1:]
y = all_data.as_matrix()[:,0]
print(cross_validation.cross_val_score(clf, X, y, cv=5))
'''
���ݷָ�
'''
# �ָ����ݣ����� ѵ������:cv���� = 7:3�ı���
split_train, split_cv = cross_validation.train_test_split(df, test_size=0.3, random_state=0)
train_df = split_train.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
# ����ģ��
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(train_df.as_matrix()[:,1:], train_df.as_matrix()[:,0])

# ��cross validation���ݽ���Ԥ��

cv_df = split_cv.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
predictions = clf.predict(cv_df.as_matrix()[:,1:])

origin_data_train = pd.read_csv("F:/Kaggle/titanic/Train.csv")
bad_cases = origin_data_train.loc[origin_data_train['PassengerId'].isin(split_cv[predictions != cv_df.as_matrix()[:,0]]['PassengerId'].values)]
bad_cases
'''
ѧϰ�����߻���
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.learning_curve import learning_curve

# ��sklearn��learning_curve�õ�training_score��cv_score��ʹ��matplotlib����learning curve
def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=1,
                        train_sizes=np.linspace(.05, 1., 20), verbose=0, plot=True):
    """
    ����data��ĳģ���ϵ�learning curve.
    ��������
    ----------
    estimator : ���õķ�������
    title : ���ı��⡣
    X : �����feature��numpy����
    y : �����target vector
    ylim : tuple��ʽ��(ymin, ymax), �趨ͼ�������������͵����ߵ�
    cv : ��cross-validation��ʱ�����ݷֳɵķ���������һ����Ϊcv��������n-1����Ϊtraining(Ĭ��Ϊ3��)
    n_jobs : ���еĵ�������(Ĭ��1)
    """
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes, verbose=verbose)

    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    if plot:
        plt.figure()
        plt.title(title)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.xlabel(u"ѵ��������")
        plt.ylabel(u"�÷�")
        plt.gca().invert_yaxis()
        plt.grid()

        plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,
                         alpha=0.1, color="b")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std,
                         alpha=0.1, color="r")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="b", label=u"ѵ�����ϵ÷�")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="r", label=u"������֤���ϵ÷�")

        plt.legend(loc="best")

        plt.draw()
        plt.show()
        plt.gca().invert_yaxis()

    midpoint = ((train_scores_mean[-1] + train_scores_std[-1]) + (test_scores_mean[-1] - test_scores_std[-1])) / 2
    diff = (train_scores_mean[-1] + train_scores_std[-1]) - (test_scores_mean[-1] - test_scores_std[-1])
    return midpoint, diff

plot_learning_curve(clf, u"ѧϰ����", X, y)

'''
����bagging��������ѵ�����Ĳ�ַ�ֹ�����
'''
if __name__=='__main__':
    train_df = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass.*|Mother|Child|Family|Title')
    train_np = train_df.as_matrix()

    # y��Survival���
    y = train_np[:, 0]

    # X����������ֵ
    X = train_np[:, 1:]

    # fit��BaggingRegressor֮��
    clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
    bagging_clf = BaggingRegressor(clf, n_estimators=20, max_samples=0.8, max_features=1.0, bootstrap=True, bootstrap_features=False, n_jobs=-1)
    bagging_clf.fit(X, y)

    test = df_test.filter(regex='Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass.*|Mother|Child|Family|Title')
    predictions = bagging_clf.predict(test)
    result = pd.DataFrame({'PassengerId':data_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
    result.to_csv("F:/Kaggle/titanic/logistic_regression_bagging_predictions.csv", index=False)