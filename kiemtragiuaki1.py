import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def bieu_do1():
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5']
    doanh_so = [100, 150, 200, 250, 300]

    plt.plot(thang, doanh_so)
    plt.title('Doanh số bán hàng theo tháng')
    plt.xlabel('Tháng')
    plt.ylabel('Doanh số')
    plt.show()
def bieu_do2():
    # Dữ liệu ví dụ
    years = [2000, 2001, 2002, 2003, 2004, 2005]
    yield_data = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    plt.plot(years, yield_data)
    plt.title('Sản lượng cây trồng theo năm')
    plt.xlabel('Năm')
    plt.ylabel('Sản lượng (tấn trên héc ta)')
    plt.show()
def bieu_do3():
    import matplotlib.pyplot as plt

    # Tạo Figure
    fig = plt.figure()

    # Thêm Axes
    ax = fig.add_subplot(1, 1, 1)

    # Vẽ biểu đồ
    ax.plot([1, 2, 3], [1, 4, 9])
    ax.set_title('Biểu đồ đường')
    ax.set_xlabel('Trục x')
    ax.set_ylabel('Trục y')

    # Hiển thị biểu đồ
    plt.show()
def bieu_do4():
    # Dữ liệu
    ngay = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ nhật']
    nhiet_do = [22, 24, 20, 23, 25, 26, 24]

    # Vẽ biểu đồ
    plt.plot(ngay, nhiet_do)
    plt.title('Nhiệt độ hàng ngày')
    plt.xlabel('Ngày')
    plt.ylabel('Nhiệt độ (°C)')
    plt.figure(figsize=(10, 5))
    plt.show()
def bieu_do5():
    A = [1, 2, 3, 6, 10]
    B = [4, 4, 7, 8, 8]
    C = [9, 3, 4, 5, 6]

    plt.plot(A, B, 'b', label='blue points')  # Đường màu xanh
    plt.plot(C, B, 'r', label='red points')  # Đường màu đỏ
    plt.title("Graph Title")  # Tiêu đề biểu đồ
    plt.xlabel("Horizontal Axis")  # Nhãn trục hoành
    plt.ylabel("Vertical Axis")  # Nhãn trục tung
    plt.show()  # Hiển thị biểu đồ
def bieu_do6():
    x = np.arange(-5, 5, 0.001)
    y = x ** 3

    plt.figure(figsize=(5, 2))
    plt.plot(x, y, 'b')
    plt.title("Function Plot y = x^3")
    plt.xlabel("Horizontal Axis")
    plt.ylabel("Vertical Axis")
    plt.show()
def bieu_do7():
    x = np.arange(-5, 5, 0.0001)
    y = x ** 2
    z = x ** 3

    plt.figure(figsize=(5.5, 2))
    plt.subplot(1, 2, 1)  # 1 hàng, 2 cột, biểu đồ đầu tiên
    plt.plot(x, y, 'b')  # Biểu đồ màu xanh
    plt.subplot(1, 2, 2)  # 1 hàng, 2 cột, biểu đồ thứ hai
    plt.plot(x, z, 'r')  # Biểu đồ màu đỏ
    plt.show()
def bieu_do8():
    categories = ['Excellent', 'Good', 'Average', 'Weak', 'Poor']
    values = [25, 55, 10, 6, 4]

    plt.bar(categories, values)
    plt.title("Student Performance Classification")
    plt.xlabel("Performance Level")
    plt.ylabel("Number of Students")
    plt.show()
def bieu_do9():
    from matplotlib import pyplot as plt

    categories = ['Excellent', 'Good', 'Average', 'Weak', 'Poor']
    values = [25, 55, 41, 30, 50]

    plt.pie(values, labels=categories)
    plt.title("Pie Chart")
    plt.show()
def doc_file():
    cities = pd.read_csv("california_cities.csv")
    print(cities.columns)
def bieu_do10():
    # Load data from CSV
    cities = pd.read_csv("california_cities.csv")

    # Calculate population density (people per square kilometer)
    cities['density'] = cities['population_total'] / cities['area_total_km2']

    # Select the top 15 cities with the highest population density
    top_density = cities.sort_values(by='density', ascending=False).head(15)

    # Plot horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(top_density['city'], top_density['density'], color='coral')
    plt.xlabel('Population Density (people/km²)')
    plt.title('Top 15 Most Densely Populated Cities in California')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
def bieu_do11():

    # Load data
    cities = pd.read_csv("california_cities.csv")
    population = cities['population_total']

    # Create histogram using log10(population) for better visualization
    plt.figure(figsize=(8, 6))
    plt.hist(np.log10(population), bins=30, color='orange', edgecolor='black')
    plt.xlabel('log10(Population)')
    plt.ylabel('Number of Cities')
    plt.title('Distribution of City Populations in California (Log Scale)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
def bieu_do12():
    cities = pd.read_csv("california_cities.csv")
    lat, lon = cities['latd'], cities['longd']
    population = cities['population_total']
    area = cities['area_total_km2']

    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(8, 6))
    plt.scatter(lon, lat, c=np.log10(population), cmap='viridis',
                s=area, linewidths=0, alpha=0.5)
    plt.axis('equal')
    plt.xlabel('longtitude')
    plt.ylabel('latitude')
    plt.title('California Cities: Population and Area Distribution')
    plt.colorbar(label='log$_{10}$(population)')
    plt.show()
doc_file()
bieu_do1()
bieu_do2()
bieu_do3()
bieu_do4()
bieu_do5()
bieu_do6()
bieu_do7()
bieu_do8()
bieu_do9()
bieu_do10()
bieu_do11()
bieu_do12()