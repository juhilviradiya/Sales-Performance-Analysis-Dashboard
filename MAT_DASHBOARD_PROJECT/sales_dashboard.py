project = pd.read_excel(r'/content/Matplotlib_Final_Project.xlsx')
plt.figure(figsize=(16,12),facecolor='#F5F7FA')
plt.subplot(2,2,1)
month = project.groupby('Month')['Revenue'].sum()
plt.plot(month,
         color='#2563EB',
         marker='o',
         markersize=6,
         markeredgecolor='#1E3A8A',
         markerfacecolor='#F59E0B',
         linewidth=1.8,
         label='MONTHLY REVENUE')

plt.legend()
plt.xticks(rotation=45)
plt.xlabel('MONTH', fontsize=10, color='#334155')
plt.ylabel('REVENUE', fontsize=10, color='#334155')
plt.grid(alpha=0.25, color='#94A3B8')
plt.title('MONTHLY REVENUE', color='#0F172A')
plt.tight_layout()


# BAR PLOT
plt.subplot(2,2,2)

new = project.groupby('Region')['Revenue'].sum()

plt.bar(new.index, new.values,label='REGION WISE REVENUE',
        edgecolor='#1E3A8A',
        linestyle='--',
        color='#3B82F6',
        linewidth=1.5
        )
plt.legend(fontsize=8)

plt.xlabel('REGION', fontsize=10, color='#334155')
plt.ylabel('REVENUE', fontsize=10, color='#334155')
plt.xticks(rotation=45)
plt.yticks(fontsize=8)
plt.title('REGION WISE REVENUE', color='#0F172A')
plt.grid(axis='y', alpha=0.25, color='#94A3B8')

plt.tight_layout()


# HORIZONTAL BAR CHART
plt.subplot(2,2,3)

product = project.groupby('Product')['Profit'].sum()
product = product.sort_values(ascending=True).tail(10)

plt.barh(product.index, product.values,
         color='#3B82F6',
         label='PRODUCT WISE PROFIT',
         edgecolor='#1E3A8A',
         linewidth=1.5
         )

plt.legend()
plt.xlabel('PROFIT', fontsize=10, color='#334155')
plt.ylabel('PRODUCT', fontsize=10, color='#334155')

plt.title('TOP 10 PRODUCTS BY PROFIT', color='#0F172A')
plt.grid(axis='x', alpha=0.25)

plt.yticks(fontsize=10)
plt.xticks(fontsize=8)




# PIE-CHART
plt.subplot(2,2,4)

channel = project.groupby('Sales_Channel')['Revenue'].sum()

plt.pie(channel.values, labels=channel.index,
        autopct='%0.1f%%',
        startangle=90,
        colors = ['#2563EB', '#F59E0B', '#10B981'],
        wedgeprops={'edgecolor': '#FFFFFF', 'linewidth': 2})

plt.title('SALES CHANNEL REVENUE')
plt.suptitle('SALES PERFORMANCE ANALYSIS DASHBOARD',
             fontsize=18,
             fontweight='bold',
             color='#0F172A')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('SALES_PERFORMANCE.png',dpi=300)
plt.show()
