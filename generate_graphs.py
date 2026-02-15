import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def generate_oppgave1():
    t1 = np.linspace(0, 1.20, 100)
    v1 = np.full_like(t1, 0.20)

    t2 = np.linspace(1.20, 1.20 + 1.54, 100)
    v2 = 0.20 - (0.20 / 1.54) * (t2 - 1.20)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

    ax1.plot(t1, v1, 'b-', linewidth=2.2, label='Konstant fart (flat strekning)')
    ax1.plot(t2, v2, 'r-', linewidth=2.2, label='Retardasjon (motbakke)')
    ax1.axvline(x=1.20, color='gray', linestyle='--', alpha=0.5, label='Overgang til motbakke')
    ax1.axhline(y=0, color='black', linewidth=0.5)

    ax1.annotate('v = 0.20 m/s', xy=(0.6, 0.20), xytext=(0.6, 0.24),
                 fontsize=9, color='blue',
                 arrowprops=dict(arrowstyle='->', color='blue'),
                 ha='center')

    ax1.annotate('v = 0 m/s\n(bilen stopper)', xy=(2.74, 0), xytext=(2.50, 0.08),
                 fontsize=9, color='red',
                 arrowprops=dict(arrowstyle='->', color='red'),
                 ha='center')

    ax1.set_xlabel('Tid [s]')
    ax1.set_ylabel('Hastighet [m/s]')
    ax1.set_title('Hastighet som funksjon av tid', fontsize=12)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlim(-0.05, 1.20 + 1.54 + 0.1)
    ax1.set_ylim(-0.03, 0.20 + 0.08)
    ax1.grid(True, alpha=0.3)

    ax1.text(0.6, 0.92, 'Fase 1:\nFlat strekning', transform=ax1.get_xaxis_transform(),
             fontsize=8, fontstyle='italic', color='gray', ha='center', va='top')
    ax1.text(1.97, 0.92, 'Fase 2:\nMotbakke', transform=ax1.get_xaxis_transform(),
             fontsize=8, fontstyle='italic', color='gray', ha='center', va='top')

    t_step = [0, 1.20, 1.20, 2.74]
    a_step = [0, 0, -0.130, -0.130]
    ax2.step(t_step, a_step, where='post', color='purple', linewidth=2.2)

    ax2.fill_between([1.20, 2.74], -0.130, 0, alpha=0.15, color='purple')

    ax2.axhline(y=0, color='black', linewidth=0.5)
    ax2.axvline(x=1.20, color='gray', linestyle='--', alpha=0.5)

    ax2.annotate('a = 0 m/s²\n(ingen akselerasjon)', xy=(0.6, 0), xytext=(0.6, 0.04),
                 fontsize=9, color='green', ha='center')

    ax2.annotate('a = -0.130 m/s²\n(retardasjon)', xy=(1.97, -0.130), xytext=(1.97, -0.06),
                 fontsize=9, color='purple',
                 arrowprops=dict(arrowstyle='->', color='purple'),
                 ha='center')

    ax2.set_xlabel('Tid [s]')
    ax2.set_ylabel('Akselerasjon [m/s²]')
    ax2.set_title('Akselerasjon som funksjon av tid', fontsize=12)
    ax2.set_xlim(-0.05, 2.84)
    ax2.set_ylim(-0.130 - 0.08, 0.08)
    ax2.grid(True, alpha=0.3)

    ax2.text(0.6, 0.92, 'Fase 1:\nFlat strekning', transform=ax2.get_xaxis_transform(),
             fontsize=8, fontstyle='italic', color='gray', ha='center', va='top')
    ax2.text(1.97, 0.92, 'Fase 2:\nMotbakke', transform=ax2.get_xaxis_transform(),
             fontsize=8, fontstyle='italic', color='gray', ha='center', va='top')

    fig.suptitle('Oppgave 1: Bilens bevegelse', fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    plt.savefig('oppgave1_grafer.png', dpi=200)
    plt.close()
    print('Generert: oppgave1_grafer.png')


def generate_oppgave2():
    kategorier = ['1 meter', '2 meter']
    falltid_forsok = [0.35, 0.67]
    falltid_teori = [0.452, 0.639]
    akselerasjon_forsok = [16.33, 8.91]
    akselerasjon_teori = [9.81, 9.81]
    slutthastighet_forsok = [5.71, 5.97]
    slutthastighet_teori = [4.43, 6.26]

    data_sets = [
        ('Falltid', 'Tid [s]', falltid_forsok, falltid_teori),
        ('Akselerasjon', 'Akselerasjon [m/s²]', akselerasjon_forsok, akselerasjon_teori),
        ('Slutthastighet', 'Hastighet [m/s]', slutthastighet_forsok, slutthastighet_teori)
    ]

    fig, axes = plt.subplots(1, 3, figsize=(10, 4))

    x = np.arange(2)
    bar_width = 0.30

    for ax, (title, ylabel, forsok, teori) in zip(axes, data_sets):
        bars1 = ax.bar(x - bar_width/2, forsok, bar_width,
                       color='#e74c3c', alpha=0.8, edgecolor='black',
                       linewidth=0.5, label='Forsøk')
        bars2 = ax.bar(x + bar_width/2, teori, bar_width,
                       color='#3498db', alpha=0.8, edgecolor='black',
                       linewidth=0.5, label='Teori')

        for bar in bars1:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(bar.get_x() + bar.get_width()/2, height),
                        xytext=(0, 3), textcoords='offset points',
                        ha='center', va='bottom', fontsize=7.5)

        for bar in bars2:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(bar.get_x() + bar.get_width()/2, height),
                        xytext=(0, 3), textcoords='offset points',
                        ha='center', va='bottom', fontsize=7.5)

        ax.set_title(title)
        ax.set_xlabel('Fallhøyde', fontsize=9)
        ax.set_ylabel(ylabel)
        ax.set_xticks(x)
        ax.set_xticklabels(kategorier)
        ax.legend(fontsize=8)
        ax.yaxis.grid(True, alpha=0.3)
        ax.set_axisbelow(True)

    fig.suptitle('Oppgave 2: Sammenligning av teoretiske og eksperimentelle verdier',
                 fontsize=12, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.92])

    plt.savefig('oppgave2_sammenligning.png', dpi=200)
    plt.close()
    print('Generert: oppgave2_sammenligning.png')


if __name__ == '__main__':
    generate_oppgave1()
    generate_oppgave2()
    print('Ferdig! Begge grafene er generert.')
